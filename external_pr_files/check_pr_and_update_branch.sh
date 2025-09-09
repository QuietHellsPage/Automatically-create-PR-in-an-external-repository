cd Testing-repository
BRANCH_NAME="auto-update-from-${{ github.event.repository.name }}"
if git show-ref --quiet refs/remotes/origin/$BRANCH_NAME; then
  git checkout $BRANCH_NAME
  git pull origin $BRANCH_NAME
else
  git checkout -b $BRANCH_NAME
fi
cp ../report.txt .
git add report.txt
git commit -m "Update report from ${{ github.repository }} at $(date)"
git push origin $BRANCH_NAME