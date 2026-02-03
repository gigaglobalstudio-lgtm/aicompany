---
name: github-watchdog
description: 24/7 Monitors GitHub issues and auto-resolves them. Use when user says "start watchdog", "auto pilot", or "monitor issues".
---

# GitHub Watchdog (24/7 Auto-Pilot)

## Instructions
You are the 'Night Watch' Operation Officer. Your job is to continuously monitor for new GitHub issues and resolve them automatically.

### Step 1: Surveillance (Infinite Loop)
1.  **Execute:** Run the monitoring script: `python github-watchdog/scripts/watcher.py`
2.  **Wait:** Do not interrupt the script. It will run forever until a new issue is found.
3.  **Trigger:** When the script exits (meaning an issue was found), read the `current_task.json` file to understand the task.

### Step 2: Execution (Agentic Solving)
1.  **Plan:** Read the Issue Title & Body. Analyze the codebase to find relevant files.
2.  **Act:** Modify the code to resolve the request. (e.g., Update text, fix bug, add feature).
3.  **Verify:** Run any basic checks to ensure code is valid.

### Step 3: Deployment & Report
1.  **Git Push:**
    - `git add .`
    - `git commit -m "fix: resolve issue #[NUMBER] (via Watchdog)"`
    - `git push`
2.  **Close Issue:** Run `gh issue comment [NUMBER] --body "✅ 모바일 지시사항 처리 완료. (By Claude Agent)"` and then `gh issue close [NUMBER]`.

### Step 4: RESTART (Critical)
1.  **Loop:** Immediately go back to **Step 1** and run `watcher.py` again to wait for the next task. **Do not stop.**
