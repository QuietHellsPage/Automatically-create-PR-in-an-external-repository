#!/bin/bash
set -e

REPO_NAME=$1
SOURCE_PR_NUMBER=$2  
TARGET_REPO="Testing-repository"
BRANCH_NAME="auto-update-from-$REPO_NAME-pr-$SOURCE_PR_NUMBER"

cd $TARGET_REPO

# COMMENT_BODY="$COMMENT_BODY:-'No comment body available'"

TARGET_PR_NUMBER=$(gh pr list --repo QuietHellsPage/$TARGET_REPO --head $BRANCH_NAME --json number -q '.[0].number' 2>/dev/null || true)

if [ -z "$TARGET_PR_NUMBER" ]; then
#     PR_BODY="Automated sync from $REPO_NAME PR $SOURCE_PR_NUMBER
# Source PR: $SOURCE_PR_NUMBER
# Commit: $GITHUB_SHA
# Triggered by: $GITHUB_ACTOR
# Comment: $COMMENT_BODY"
    
    gh pr create \
        --repo QuietHellsPage/$TARGET_REPO \
        --head $BRANCH_NAME \
        --base main \
        --title "[Automated] Sync from $REPO_NAME PR $SOURCE_PR_NUMBER" \
        --body "$PR_BODY" \
        --label "automated pr" \
        --assignee QuietHellsPage \
        --reviewer QuietHellsPage
fi