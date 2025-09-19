#!/bin/bash
set -e

REPO_NAME=$1
PR_NUMBER=$2
TARGET_REPO="Testing-repository"
BRANCH_NAME="auto-update-from-$REPO_NAME-pr-$PR_NUMBER"

echo "Starting script with parameters:"
echo "REPO_NAME: $REPO_NAME"
echo "PR_NUMBER: $PR_NUMBER"
echo "TARGET_REPO: $TARGET_REPO"
echo "BRANCH_NAME: $BRANCH_NAME"

cd $TARGET_REPO

git config user.name "github-actions[bot]"
git config user.email "41898282+github-actions[bot]@users.noreply.github.com"

if git show-ref --quiet refs/remotes/origin/$BRANCH_NAME; then
    echo "Branch $BRANCH_NAME exists, checking out..."
    git checkout $BRANCH_NAME
    git pull origin $BRANCH_NAME
else
    echo "Branch $BRANCH_NAME does not exist, creating new branch..."
    git checkout -b $BRANCH_NAME
fi

PR_BRANCH=$(gh pr view $PR_NUMBER --repo $GITHUB_REPOSITORY --json headRefName --jq '.headRefName' 2>/dev/null || echo "")
echo "PR_BRANCH: $PR_BRANCH"

if [ -z "$PR_BRANCH" ]; then
    echo "Error: Could not get PR branch information"
    exit 1
fi

echo "Adding parent-repo remote..."
git remote add parent-repo https://github.com/$GITHUB_REPOSITORY.git
echo "Fetching from parent-repo..."
git fetch parent-repo

CHANGED_FILES=$(gh pr view $PR_NUMBER --repo $GITHUB_REPOSITORY --json files --jq '.files[].path' 2>/dev/null || echo "")
echo "CHANGED_FILES: $CHANGED_FILES"

if [ -z "$CHANGED_FILES" ]; then
    echo "No changed files found in PR"
    exit 0
fi

echo "Checking bom.txt in parent-repo/$PR_BRANCH"
BOM_EXISTS=false
if git show parent-repo/$PR_BRANCH:bom.txt &>/dev/null; then
    echo "bom.txt exists in the PR branch"
    BOM_EXISTS=true
    BOM_FILES=$(git show parent-repo/$PR_BRANCH:bom.txt 2>/dev/null | grep -v '^$' || echo "")
    echo "BOM_FILES contents:"
    echo "$BOM_FILES"
else
    echo "bom.txt does not exist in the PR branch"
    BOM_EXISTS=false
    BOM_FILES=""
fi

echo "BOM_EXISTS: $BOM_EXISTS"

HAS_CHANGES=false

for file in $CHANGED_FILES; do
    echo "Processing file: $file"
    if [ "$BOM_EXISTS" = true ] && (echo "$BOM_FILES" | grep -q "^$file$" || echo "$BOM_FILES" | grep -q "^\./$file$"); then
        echo "File $file found in bom.txt, proceeding..."
        mkdir -p "$(dirname "$file")"
        if git show parent-repo/$PR_BRANCH:"$file" > "$file" 2>/dev/null; then
            git add "$file"
            HAS_CHANGES=true
            echo "Added $file - found in bom.txt"
        else
            echo "Failed to get file $file from parent-repo"
        fi
    else
        echo "Skipping $file - bom.txt doesn't exist or file not in bom.txt"
    fi
done

PR_DELETED_FILES=$(gh pr view $PR_NUMBER --repo $GITHUB_REPOSITORY --json files --jq '.files[] | select(.status == "removed") | .path' 2>/dev/null || echo "")
echo "PR_DELETED_FILES: $PR_DELETED_FILES"

for deleted_file in $PR_DELETED_FILES; do
    echo "Processing deleted file: $deleted_file"
    if [ "$BOM_EXISTS" = true ] && (echo "$BOM_FILES" | grep -q "^$deleted_file$" || echo "$BOM_FILES" | grep -q "^\./$deleted_file$"); then
        echo "Deleted file $deleted_file found in bom.txt, proceeding..."
        if [ -f "$deleted_file" ]; then
            git rm "$deleted_file" 2>/dev/null || rm "$deleted_file"
            HAS_CHANGES=true
            echo "Removed $deleted_file - found in bom.txt"
        else
            echo "File $deleted_file not found locally, skipping removal"
        fi
    else
        echo "Skipping deletion of $deleted_file - bom.txt doesn't exist or file not in bom.txt"
    fi
done

if [ "$HAS_CHANGES" = true ]; then
    echo "Committing changes..."
    git commit -m "Sync changes from $REPO_NAME PR $PR_NUMBER"
    echo "Pushing to origin $BRANCH_NAME..."
    git push origin $BRANCH_NAME
    echo "Changes pushed successfully"
else
    echo "No changes to commit"
fi

echo "Script completed successfully"