#!/bin/bash
set -e

REPO_NAME=$1
PR_NUMBER=$2
TARGET_REPO="Testing-repository"
BRANCH_NAME="auto-update-from-$REPO_NAME-pr-$PR_NUMBER"

cd $TARGET_REPO

PR_NUMBER=$(gh pr list --repo QuietHellsPage/$TARGET_REPO --head $BRANCH_NAME --json number -q '.[0].number' 2>/dev/null || true)

if [ -z "$PR_NUMBER" ]; then
    gh pr create \
        --repo QuietHellsPage/$TARGET_REPO \
        --head $BRANCH_NAME \
        --base main \
        --title "[Automated] Sync from $REPO_NAME PR #$PR_NUMBER" \
        --body "Automated sync from $REPO_NAME PR #$PR_NUMBER
        Source PR: #$PR_NUMBER
        Merge commit: $GITHUB_SHA
        Triggered by: $GITHUB_ACTOR" \
        --label "automated pr" \
        --assignee QuietHellsPage \
        --reviewer QuietHellsPage
else
    gh pr comment $PR_NUMBER --repo QuietHellsPage/$TARGET_REPO --body "Automatically updated at $(date)"
fi
