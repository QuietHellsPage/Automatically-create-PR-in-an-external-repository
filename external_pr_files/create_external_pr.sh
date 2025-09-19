#!/bin/bash
set -e

SOURCE_REPO="$1"
PR_NUMBER="$2"

bash external_pr_files/clone_target_repo.sh

bash external_pr_files/create_label.sh

bash external_pr_files/check_pr_and_update_branch.sh "$SOURCE_REPO" "$PR_NUMBER"

bash external_pr_files/create_or_update_pr.sh "$SOURCE_REPO" "$PR_NUMBER"
