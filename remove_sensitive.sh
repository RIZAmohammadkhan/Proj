#!/bin/bash

# Remove .env file from Git history
git filter-branch --force --index-filter \
  "git rm --cached --ignore-unmatch .env" \
  --prune-empty --tag-name-filter cat -- --all

# Remove database files
git filter-branch --force --index-filter \
  "git rm --cached --ignore-unmatch instance/prompts.db" \
  --prune-empty --tag-name-filter cat -- --all

git filter-branch --force --index-filter \
  "git rm --cached --ignore-unmatch *.sqlite" \
  --prune-empty --tag-name-filter cat -- --all

# Remove migrations folder
git filter-branch --force --index-filter \
  "git rm -r --cached --ignore-unmatch migrations/" \
  --prune-empty --tag-name-filter cat -- --all

# Force push changes
echo "Now run: git push origin --force --all" 