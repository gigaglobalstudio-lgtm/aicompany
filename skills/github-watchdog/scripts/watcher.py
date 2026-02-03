import time
import subprocess
import json
import sys
import os

# Set UTF-8 encoding for Windows
os.environ['PYTHONIOENCODING'] = 'utf-8'

def watch_issues():
    print("[Watchdog] GitHub Issue Monitoring... (60s interval)")
    print("   (Create an issue from your phone to trigger)")

    while True:
        try:
            result = subprocess.run(
                ["gh", "issue", "list", "--state", "open", "--limit", "1", "--json", "number,title,body"],
                capture_output=True,
                encoding='utf-8',
                errors='replace'
            )

            if result.returncode != 0:
                print("[ERROR] GitHub CLI Error: Run 'gh auth login' first.")
                time.sleep(60)
                continue

            issues = json.loads(result.stdout)

            if issues:
                issue = issues[0]
                print(f"\n[DETECTED] New Issue Found! #{issue['number']}: {issue['title']}")
                print(">>> Starting agent task...")
                with open("current_task.json", "w", encoding="utf-8") as f:
                    json.dump(issue, f, ensure_ascii=False, indent=2)
                sys.exit(0)

            print(".", end="", flush=True)
            time.sleep(60)

        except Exception as e:
            print(f"Error: {e}")
            time.sleep(60)

if __name__ == "__main__":
    watch_issues()
