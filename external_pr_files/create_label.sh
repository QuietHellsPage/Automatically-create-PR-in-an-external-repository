cd Testing-repository
if ! gh label list --repo QuietHellsPage/Testing-repository --json name -q '.[] | select(.name == "automated pr")' | grep -q "automated pr"; then
  gh label create "automated pr" --color "0E8A16" --description "Automated pull request" --repo QuietHellsPage/Testing-repository
fi