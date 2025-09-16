#!/bin/bash
set -e

REPO_NAME=$1
PR_NUMBER=$2
TARGET_REPO="Testing-repository"
BRANCH_NAME="auto-update-from-$REPO_NAME-pr-$PR_NUMBER"

echo "Starting sync process from $REPO_NAME PR $PR_NUMBER"
echo "Branch name: $BRANCH_NAME"

cd $TARGET_REPO

git config user.name "github-actions[bot]"
git config user.email "41898282+github-actions[bot]@users.noreply.github.com"

if git show-ref --quiet refs/remotes/origin/$BRANCH_NAME; then
    echo "Branch $BRANCH_NAME exists, checking out..."
    git checkout $BRANCH_NAME
    git pull origin $BRANCH_NAME
else
    echo "Creating new branch $BRANCH_NAME..."
    git checkout -b $BRANCH_NAME
fi

echo "Getting changed files from PR $PR_NUMBER..."

CHANGED_FILES=$(gh pr view $PR_NUMBER --repo $GITHUB_REPOSITORY --json files --jq '.files.[].path' 2>/dev/null || echo "")

if [ -z "$CHANGED_FILES" ]; then
    echo "No changed files found in PR or error fetching file list"
    exit 0
fi

echo "Changed files in PR:"
echo "$CHANGED_FILES"

echo "Copying only changed files from PR..."
for file in $CHANGED_FILES; do
    if [ -f "../$file" ]; then
        echo "Copying $file..."
        mkdir -p "$(dirname "$file")"
        cp "../$file" "$file"
    else
        echo "File $file not found in parent repository, might be deleted in PR"
    fi
done

echo "Checking for deleted files in PR..."
PR_FILE_STATUS=$(gh pr view $PR_NUMBER --repo $GITHUB_REPOSITORY --json files --jq '.files[] | select(.status == "removed") | .path' 2>/dev/null || echo "")

for deleted_file in $PR_FILE_STATUS; do
    if [ -f "$deleted_file" ]; then
        echo "Removing $deleted_file (deleted in PR)..."
        rm "$deleted_file"
    fi
done

git add .

git commit -m "Sync changes from $REPO_NAME PR $PR_NUMBER" || echo "No changes to commit"

git push origin $BRANCH_NAME

echo "Branch $BRANCH_NAME updated successfully with PR changes"