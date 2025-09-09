#!/bin/bash
set -e

TARGET_REPO="Testing-repository"

git clone https://$GH_TOKEN@github.com/QuietHellsPage/$TARGET_REPO.git
cd $TARGET_REPO
git config user.name "github-actions[bot]"
git config user.email "41898282+github-actions[bot]@users.noreply.github.com"