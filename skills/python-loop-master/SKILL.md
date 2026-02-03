---
name: python-loop-master
description: Writes code, RUNS it to check for errors, and fixes it automatically. Use for "write python", "data analysis", "create calculator", "코드 실행", or "파이썬 스크립트".
---

# Python Loop Master (Self-Healing)

## Overview
You are a Senior Developer. Do not just write code; **Ensure it runs without errors.**

## Instructions

### Step 1: Draft (초안 작성)
1. **Understand** the user's goal completely
2. **Plan** the solution approach
3. **Write** the Python script
4. **Save** to file (e.g., `Output/script.py`)

### Step 2: Verification Loop (핵심: 검증 루프)

```
┌─────────────────────────────────────────────────────────┐
│                  VERIFICATION LOOP                      │
│                                                         │
│   ┌──────────┐                                         │
│   │  Write   │                                         │
│   │  Code    │                                         │
│   └────┬─────┘                                         │
│        │                                               │
│        ▼                                               │
│   ┌──────────┐      ┌──────────┐                      │
│   │   Run    │──────│  Error?  │                      │
│   │  python  │      └────┬─────┘                      │
│   └──────────┘           │                            │
│                    Yes   │   No                       │
│                    ┌─────┴─────┐                      │
│                    │           │                      │
│                    ▼           ▼                      │
│              ┌──────────┐ ┌──────────┐               │
│              │  Analyze │ │ Success! │               │
│              │ Traceback│ │  Done    │               │
│              └────┬─────┘ └──────────┘               │
│                   │                                   │
│                   ▼                                   │
│              ┌──────────┐                            │
│              │  Rewrite │◄─── Loop back (max 3x)    │
│              │   Code   │                            │
│              └──────────┘                            │
│                                                       │
└─────────────────────────────────────────────────────────┘
```

**CRITICAL: You must EXECUTE the code to verify it.**

1. **Run:** Execute `python script.py`
2. **Check:**
   - **IF Error:**
     - Read the traceback carefully
     - Analyze *why* it failed
     - **Rewrite the code** to fix the bug
     - Go back to 'Run'
   - **IF Success:**
     - Verify output matches user's requirement
     - Proceed to Final Output
3. **Limit:** Repeat this loop up to **3 times** if errors persist

### Step 3: Final Output
```
IF successful:
  → "✅ 검증 완료. 코드가 정상 작동합니다."
  → Show the working code
  → Show the output

IF failed after 3 tries:
  → "❌ 3회 시도 후에도 에러 발생"
  → Show error log
  → Ask for human intervention
```

## Error Analysis Protocol

When an error occurs, analyze:

| Error Type | Common Cause | Fix Strategy |
|------------|--------------|--------------|
| SyntaxError | Typo, missing colon | Check syntax carefully |
| ImportError | Module not installed | pip install or fix import |
| NameError | Undefined variable | Define before use |
| TypeError | Wrong type passed | Type conversion or check |
| IndexError | Out of range | Check list length |
| KeyError | Dict key missing | Use .get() or check key |
| FileNotFoundError | Path issue | Verify path exists |
| ZeroDivisionError | Division by zero | Add zero check |

## Example Workflow

```
User: "1부터 100까지 소수 찾는 코드 만들어줘"

[Step 1: Draft]
→ Write prime number finder script
→ Save to Output/primes.py

[Step 2: Run - Attempt 1]
→ python Output/primes.py
→ Error: IndentationError at line 5

[Step 2: Fix]
→ Analyze: Missing indentation in for loop
→ Rewrite: Fix indentation
→ Save updated code

[Step 2: Run - Attempt 2]
→ python Output/primes.py
→ Success! Output: [2, 3, 5, 7, 11, ...]

[Step 3: Final Output]
→ "✅ 검증 완료. 코드가 정상 작동합니다."
→ Display working code and output
```

## Code Template

```python
#!/usr/bin/env python3
"""
Script: [description]
Author: AI-HQ
Date: [auto-generated]
"""

import sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

def main():
    # Your code here
    pass

if __name__ == "__main__":
    try:
        main()
        print("✅ 실행 완료")
    except Exception as e:
        print(f"❌ 에러: {e}")
        sys.exit(1)
```

## Quick Commands

| Command | Action |
|---------|--------|
| "이 코드 실행해봐" | Run and verify |
| "에러 고쳐줘" | Fix and re-run |
| "데이터 분석 코드" | Create + verify analysis script |
| "계산기 만들어" | Create + verify calculator |

## Integration

This pattern should be applied to:
- **content-factory**: Video/HTML generation scripts
- **excel-automator**: Data processing scripts
- **financial-report**: Report generation scripts
- Any skill that produces executable code

## Key Principle

> 📌 **핵심:** "IF Error: Rewrite the code" 구문이 루프를 닫는 열쇠입니다.
> 이 말이 없으면 에이전트는 코드만 던져주고 끝냅니다.
> **반드시 실행하고, 에러 나면 고치고, 다시 실행하세요.**
