---
name: skill-creator
description: Meta-skill that creates new skills automatically. Use when user says "이런 스킬 만들어줘", "create skill", "new skill", or "스킬 생성".
---

# Skill Creator (Master Key)

## Overview
You are the Skill Factory Agent. When a user requests a new skill, you automatically:
1. Create the folder structure
2. Write the SKILL.md file
3. Add necessary scripts
4. Install to the skills directory
5. Run a verification test

## Instructions

### Step 1: Requirement Analysis
1. **Parse Request:** Extract the skill name, purpose, and trigger keywords from the user's request.
2. **Identify Components:**
   - Does it need Python scripts? (e.g., calculations, API calls)
   - Does it need web search? (e.g., research, trends)
   - Does it need file I/O? (e.g., reports, exports)
3. **Confirm:** If unclear, ask: "이 스킬의 핵심 기능이 뭔가요?"

### Step 2: Folder Structure Creation
```bash
mkdir -p ~/[skill-name]/scripts
```

### Step 3: SKILL.md Generation
Use this template structure:

```markdown
---
name: [skill-name]
description: [One-line description]. Use when user says "[trigger1]", "[trigger2]", or "[trigger3]".
---

# [Skill Name] Skill

## Instructions
[Role definition]

### Step 1: [First Phase Name]
1. [Action 1]
2. [Action 2]
3. [Action 3]

### Step 2: [Second Phase Name]
1. [Action 1]
2. [Action 2]

### Step 3: [Output Phase Name]
1. [Action 1]
2. **Output:** Save to `Output/[filename].md`

## Error Handling
- If [error condition], [fallback action].
- If [missing input], ask: "[question in Korean]"
```

### Step 4: Script Generation (if needed)
Create Python scripts in `scripts/` folder for:
- Calculations (margin, ROI, etc.)
- Data processing
- API integrations
- File conversions

### Step 5: Installation
```bash
cp -r ~/[skill-name] ~/.claude/skills/
```

### Step 6: Verification Test
1. List installed skills to confirm
2. Run a simple test of the skill's core function
3. Report: "✅ [skill-name] 스킬 설치 및 테스트 완료"

## Skill Templates

### Template A: Research Skill
```
Use for: Market analysis, trend research, competitor analysis
Components: Web search, data extraction, report generation
Output: Markdown report
```

### Template B: Automation Skill
```
Use for: Repetitive tasks, file processing, batch operations
Components: Python scripts, file I/O, loops
Output: Processed files or logs
```

### Template C: Content Skill
```
Use for: Writing, copywriting, social media
Components: Web research, text generation, multi-format output
Output: Blog posts, SNS content packages
```

### Template D: Monitoring Skill
```
Use for: Watching for changes, alerts, notifications
Components: Infinite loops, condition checks, triggers
Output: Actions when conditions are met
```

## Quick Create Commands

When user says:
- "리서치 스킬 만들어줘" → Use Template A
- "자동화 스킬 만들어줘" → Use Template B
- "콘텐츠 스킬 만들어줘" → Use Template C
- "모니터링 스킬 만들어줘" → Use Template D

## Output Format

After creating a skill, always report:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ SKILL CREATED SUCCESSFULLY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Name: [skill-name]
Location: ~/.claude/skills/[skill-name]/
Files:
  - SKILL.md
  - scripts/[if any]
Triggers: "[trigger1]", "[trigger2]"
Status: Installed & Tested
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```
