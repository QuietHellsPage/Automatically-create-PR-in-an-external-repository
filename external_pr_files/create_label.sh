#!/bin/bash
set -e

TARGET_REPO="Testing-repository"

cd $TARGET_REPO

if ! gh label list --repo QuietHellsPage/$TARGET_REPO --json name -q '.[] | select(.name == "automated pr")' | grep -q "automated pr"; then
    gh label create "automated pr" --color "0E8A16" --description "Automated pull request" --repo QuietHellsPage/$TARGET_REPO
fi
