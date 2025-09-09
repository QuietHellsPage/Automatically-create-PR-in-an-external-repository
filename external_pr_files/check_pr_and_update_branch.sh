#!/bin/bash
set -e

REPO_NAME=$1
TARGET_REPO="Testing-repository"
BRANCH_NAME="auto-update-from-$REPO_NAME"

cd $TARGET_REPO

if git show-ref --quiet refs/remotes/origin/$BRANCH_NAME; then
    git checkout $BRANCH_NAME
    git pull origin $BRANCH_NAME
else
    git checkout -b $BRANCH_NAME
fi

cp ../report.txt .
git add report.txt
git commit -m "Update report from $REPO_NAME at $(date)"
git push origin $BRANCH_NAME