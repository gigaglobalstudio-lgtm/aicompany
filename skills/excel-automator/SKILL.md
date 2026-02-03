---
name: excel-automator
description: Excel automation with Python pandas. Use when user says "엑셀 자동화", "Excel analysis", "데이터 분석", "pivot table", or "spreadsheet".
---

# Excel Automator

## Instructions
You are an Excel automation expert using Python pandas. Transform, analyze, and generate Excel files programmatically.

### Step 1: Data Input
1. **File Types Supported:**
   - .xlsx, .xls (Excel)
   - .csv (Comma-separated)
   - .json (JSON data)

2. **Input Methods:**
   - File path
   - Raw data (paste)
   - URL (web scraping)

### Step 2: Common Operations

#### Data Cleaning
```python
# Remove duplicates
df.drop_duplicates()

# Handle missing values
df.fillna(0)  # or df.dropna()

# Data type conversion
df['column'] = df['column'].astype(int)

# String cleaning
df['name'] = df['name'].str.strip().str.title()
```

#### Data Analysis
```python
# Summary statistics
df.describe()

# Group by aggregation
df.groupby('category').agg({'sales': 'sum', 'quantity': 'mean'})

# Pivot table
pd.pivot_table(df, values='sales', index='month', columns='product', aggfunc='sum')

# Filtering
df[df['sales'] > 10000]
```

#### Data Transformation
```python
# Add calculated columns
df['profit_margin'] = (df['revenue'] - df['cost']) / df['revenue'] * 100

# Date parsing
df['date'] = pd.to_datetime(df['date'])
df['month'] = df['date'].dt.month

# Merge datasets
pd.merge(df1, df2, on='id', how='left')
```

### Step 3: Output Generation

#### Excel Export
```python
# Basic export
df.to_excel('output.xlsx', index=False)

# Multiple sheets
with pd.ExcelWriter('output.xlsx') as writer:
    df1.to_excel(writer, sheet_name='Summary')
    df2.to_excel(writer, sheet_name='Details')

# Styled export (with openpyxl)
# Apply formatting, colors, borders
```

### Step 4: Script Execution
Run: `python ~/.claude/skills/excel-automator/scripts/excel_processor.py [input] [operation] [output]`

## Quick Commands
| Command | Action |
|---------|--------|
| "엑셀 합쳐줘" | Merge multiple Excel files |
| "피벗 테이블 만들어" | Create pivot table |
| "중복 제거해줘" | Remove duplicates |
| "매출 분석해줘" | Sales analysis with charts |

## Tools Required
- pandas
- openpyxl
- xlrd (for .xls files)

## Output
- Save to: `Output/excel_[operation]_[timestamp].xlsx`
- Include: Summary statistics, charts if applicable
