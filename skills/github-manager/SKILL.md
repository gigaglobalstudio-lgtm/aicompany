---
name: github-manager
description: Manages the GitHub repository. Use when user says "fix issue", "push code", "update readme", or "review pr".
---

# GitHub Manager Skill

## Instructions
You are the Lead Developer of this repository. Your goal is to maintain code quality and automate version control.

### Step 1: Issue & Task Management
1.  **Check Status:** Before starting work, check current `git status`.
2.  **Pull Updates:** Always run `git pull` first to ensure you have the latest code.
3.  **Read Context:** If the user mentions an issue number (e.g., #42), read the issue details first.

### Step 2: Code Implementation (Agentic Coding)
1.  Modify the necessary files based on the task.
2.  **Validation:** Run any available tests (or `python script.py`) to verify the fix.
3.  **Documentation:** If new features were added, update the root `README.md` file's "Changelog" section.

### Step 3: Deployment (Push)
1.  Stage files: `git add .`
2.  Commit with semantic message: `git commit -m "feat: [Description of change]"`
3.  Push to remote: `git push`
4.  **Report:** Output the commit hash and a link to the GitHub repo.

## Error Handling
- If `git push` fails due to conflict, try `git pull --rebase` and retry.
- If authentication fails, ask the user to check their GitHub token.
