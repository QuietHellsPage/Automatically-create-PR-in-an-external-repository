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

cp ../report.txt .

git add report.txt
git commit -m "Sync changes from $REPO_NAME PR $PR_NUMBER" || echo "No changes to commit"
git push origin $BRANCH_NAME
