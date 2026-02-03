---
name: financial-report
description: Generate comprehensive financial reports with charts. Use when user says "재무 보고서", "financial report", "월간 리포트", "매출 보고서", or "실적 분석".
---

# Financial Report Generator

## Instructions
You are a CFO-level financial analyst. Generate professional financial reports with insights.

### Step 1: Data Collection
1. **Required Inputs:**
   - Revenue (매출)
   - Expenses (비용)
   - Time period (기간)

2. **Optional Inputs:**
   - Budget/Target (예산/목표)
   - Previous period (전기 비교)
   - Cost breakdown (비용 상세)

### Step 2: Report Sections

#### Executive Summary
```
┌─────────────────────────────────────────┐
│         FINANCIAL HIGHLIGHTS            │
├─────────────────────────────────────────┤
│ Revenue:        ₩100,000,000  (+15%)    │
│ Expenses:       ₩70,000,000   (+8%)     │
│ Net Profit:     ₩30,000,000   (+32%)    │
│ Profit Margin:  30%           (+4%p)    │
└─────────────────────────────────────────┘
```

#### Income Statement (손익계산서)
```
| Item | Amount | % of Revenue |
|------|--------|--------------|
| Revenue | ₩100,000,000 | 100% |
| (-) COGS | ₩40,000,000 | 40% |
| Gross Profit | ₩60,000,000 | 60% |
| (-) Operating Expenses | ₩25,000,000 | 25% |
| Operating Income | ₩35,000,000 | 35% |
| (-) Other Expenses | ₩5,000,000 | 5% |
| Net Income | ₩30,000,000 | 30% |
```

#### Expense Breakdown
```
| Category | Amount | % |
|----------|--------|---|
| Personnel | ₩30,000,000 | 43% |
| Marketing | ₩15,000,000 | 21% |
| Operations | ₩10,000,000 | 14% |
| Technology | ₩8,000,000 | 11% |
| Other | ₩7,000,000 | 10% |
```

#### Key Metrics (KPIs)
```
| Metric | Current | Previous | Change |
|--------|---------|----------|--------|
| Revenue Growth | 15% | 12% | +3%p |
| Gross Margin | 60% | 58% | +2%p |
| Net Margin | 30% | 26% | +4%p |
| CAC | ₩50,000 | ₩55,000 | -9% |
| LTV | ₩500,000 | ₩450,000 | +11% |
| LTV/CAC | 10x | 8.2x | +22% |
```

### Step 3: Analysis & Insights

#### Trend Analysis
- Month-over-month comparison
- Year-over-year comparison
- Seasonal patterns

#### Variance Analysis
- Budget vs Actual
- Identify over/under spending
- Root cause analysis

#### Recommendations
- Cost optimization opportunities
- Growth investment areas
- Risk mitigation strategies

### Step 4: Output Generation

#### Report Formats
1. **Executive Report (1-page)**
   - Key metrics only
   - Visual charts
   - Action items

2. **Detailed Report (Full)**
   - All financial statements
   - Department breakdowns
   - Historical trends

3. **Board Presentation**
   - Google Slides format
   - Key highlights
   - Strategic recommendations

### Step 5: Script Execution
Run: `python ~/.claude/skills/financial-report/scripts/report_generator.py [data_file] [period]`

## Quick Commands
| Command | Action |
|---------|--------|
| "월간 리포트 만들어" | Monthly financial report |
| "손익계산서 생성해줘" | Income statement |
| "예산 대비 분석해줘" | Budget variance analysis |
| "YoY 비교해줘" | Year-over-year comparison |

## Output Files
- `Output/financial_report_[date].md` - Markdown report
- `Output/financial_report_[date].xlsx` - Excel with all data
- `Output/financial_report_[date].pdf` - PDF presentation (optional)

## Tools Required
- pandas (data processing)
- openpyxl (Excel export)
- matplotlib (charts, optional)
