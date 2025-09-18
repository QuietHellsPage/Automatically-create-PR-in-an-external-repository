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


for file in $CHANGED_FILES; do
    mkdir -p "$(dirname "$file")"
    git show parent-repo/$PR_BRANCH:"$file" > "$file" 2>/dev/null
done

PR_FILE_STATUS=$(gh pr view $PR_NUMBER --repo $GITHUB_REPOSITORY --json files --jq '.files[] | select(.status == "removed") | .path' 2>/dev/null || echo "")

for deleted_file in $PR_FILE_STATUS; do
    if [ -f "$deleted_file" ]; then
        rm "$deleted_file"
    fi
done

git add .

if ! git diff --cached --quiet; then
    git commit -m "Sync changes from $REPO_NAME PR $PR_NUMBER"
fi
