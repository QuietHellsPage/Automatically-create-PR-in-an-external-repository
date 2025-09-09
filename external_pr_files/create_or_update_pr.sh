cd Testing-repository
BRANCH_NAME="auto-update-from-${{ github.event.repository.name }}"
PR_NUMBER=$(gh pr list --repo QuietHellsPage/Testing-repository --head $BRANCH_NAME --json number -q '.[0].number' 2>/dev/null || true)
if [ -z "$PR_NUMBER" ]; then
  gh pr create \
    --repo QuietHellsPage/Testing-repository \
    --head $BRANCH_NAME \
    --base main \
    --title "[Automated] Updates from ${{ github.repository }}" \
    --body "Automated updates from ${{ github.repository }}
    Generated at: $(date)
    Source: ${{ github.sha }}
    Triggered by: ${{ github.actor }}" \
    --label "automated pr" \
    --assignee QuietHellsPage \
    --reviewer QuietHellsPage
else
  gh pr comment $PR_NUMBER --repo QuietHellsPage/Testing-repository --body "Automatically updated at $(date)"
fi