#!/bin/bash
set -e

REPO_NAME=$1
PR_NUMBER=$2
TARGET_REPO="Testing-repository"
BRANCH_NAME="auto-update-from-$REPO_NAME-pr-$PR_NUMBER"


cd $TARGET_REPO

git config user.name "github-actions[bot]"
git config user.email "41898282+github-actions[bot]@users.noreply.github.com"

if git show-ref --quiet refs/remotes/origin/$BRANCH_NAME; then
    git checkout $BRANCH_NAME
    git pull origin $BRANCH_NAME
else
    git checkout -b $BRANCH_NAME
fi

PR_BRANCH=$(gh pr view $PR_NUMBER --repo $GITHUB_REPOSITORY --json headRefName --jq '.headRefName' 2>/dev/null || echo "")

if [ -z "$PR_BRANCH" ]; then
    exit 1
fi

git remote add parent-repo https://github.com/$GITHUB_REPOSITORY.git
git fetch parent-repo

CHANGED_FILES=$(gh pr view $PR_NUMBER --repo $GITHUB_REPOSITORY --json files --jq '.files[].path' 2>/dev/null || echo "")

if [ -z "$CHANGED_FILES" ]; then
    exit 0
fi

BOM_EXISTS=false
if git show parent-repo/$PR_BRANCH:bom.txt &>/dev/null; then
    BOM_EXISTS=true
    BOM_FILES=$(git show parent-repo/$PR_BRANCH:bom.txt 2>/dev/null | grep -v '^$' || echo "")
fi

HAS_CHANGES=false

for file in $CHANGED_FILES; do
    if [ "$BOM_EXISTS" = true ] && (echo "$BOM_FILES" | grep -q "^$file$" || echo "$BOM_FILES" | grep -q "^\./$file$"); then
        mkdir -p "$(dirname "$file")"
        if git show parent-repo/$PR_BRANCH:"$file" > "$file" 2>/dev/null; then
            git add "$file"
            HAS_CHANGES=true
        fi
    fi
done

PR_DELETED_FILES=$(gh pr view $PR_NUMBER --repo $GITHUB_REPOSITORY --json files --jq '.files[] | select(.status == "removed") | .path' 2>/dev/null || echo "")

for deleted_file in $PR_DELETED_FILES; do
    if [ "$BOM_EXISTS" = true ] && (echo "$BOM_FILES" | grep -q "^$deleted_file$" || echo "$BOM_FILES" | grep -q "^\./$deleted_file$"); then
        if [ -f "$deleted_file" ]; then
            git rm "$deleted_file" 2>/dev/null || rm "$deleted_file"
            HAS_CHANGES=true
        fi
    fi
done

if [ "$HAS_CHANGES" = true ]; then
    git commit -m "Sync changes from $REPO_NAME PR $PR_NUMBER"
    git push origin $BRANCH_NAME
else
    echo "No changes to commit"
fi