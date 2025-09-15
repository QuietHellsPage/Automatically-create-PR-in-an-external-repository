#!/bin/bash
set -e

REPO_NAME=$1
PR_NUMBER=$2
TARGET_REPO="Testing-repository"
BRANCH_NAME="auto-update-from-$REPO_NAME-pr-$PR_NUMBER"

cd $TARGET_REPO

if git show-ref --quiet refs/remotes/origin/$BRANCH_NAME; then
    git checkout $BRANCH_NAME
    git pull origin $BRANCH_NAME
else
    git checkout -b $BRANCH_NAME
fi

cp -r ../* . || true

rm -rf .git external_pr_sh_files

git add .
git commit -m "Sync changes from $REPO_NAME PR #$PR_NUMBER"
git push origin $BRANCH_NAME