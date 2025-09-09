git clone https://${{ secrets.TARGET_REPO_PAT }}@github.com/QuietHellsPage/Testing-repository.git
cd Testing-repository
git config user.name "github-actions[bot]"
git config user.email "41898282+github-actions[bot]@users.noreply.github.com"