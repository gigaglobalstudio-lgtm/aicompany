"""
Financial Report Generator
Usage: python report_generator.py [--revenue X] [--expenses Y] [--period YYYY-MM]
"""

import sys
import os
import json
from datetime import datetime

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

try:
    import pandas as pd
    PANDAS_AVAILABLE = True
except ImportError:
    PANDAS_AVAILABLE = False

def generate_report(revenue, expenses, period=None, prev_revenue=None, prev_expenses=None):
    """Generate financial report."""

    if period is None:
        period = datetime.now().strftime('%Y-%m')

    # Calculate metrics
    gross_profit = revenue * 0.6  # Assuming 60% gross margin
    cogs = revenue - gross_profit
    operating_expenses = expenses
    net_profit = revenue - cogs - operating_expenses
    profit_margin = (net_profit / revenue) * 100 if revenue > 0 else 0

    # Previous period comparison
    if prev_revenue and prev_expenses:
        prev_net = prev_revenue - (prev_revenue * 0.4) - prev_expenses
        revenue_growth = ((revenue - prev_revenue) / prev_revenue) * 100
        profit_growth = ((net_profit - prev_net) / prev_net) * 100 if prev_net > 0 else 0
    else:
        revenue_growth = 0
        profit_growth = 0

    # Generate report
    report = f"""
{'='*60}
         FINANCIAL REPORT - {period}
{'='*60}

EXECUTIVE SUMMARY
{'-'*60}
| Metric          | Amount           | Change    |
|-----------------|------------------|-----------|
| Revenue         | W{revenue:>14,} | {'+' if revenue_growth >= 0 else ''}{revenue_growth:>6.1f}%  |
| Gross Profit    | W{gross_profit:>14,.0f} |           |
| Net Profit      | W{net_profit:>14,.0f} | {'+' if profit_growth >= 0 else ''}{profit_growth:>6.1f}%  |
| Profit Margin   | {profit_margin:>15.1f}% |           |

INCOME STATEMENT
{'-'*60}
| Item                    | Amount           | % Rev  |
|-------------------------|------------------|--------|
| Revenue                 | W{revenue:>14,} | 100.0% |
| (-) Cost of Goods Sold  | W{cogs:>14,.0f} | {(cogs/revenue*100):>5.1f}% |
| Gross Profit            | W{gross_profit:>14,.0f} | {(gross_profit/revenue*100):>5.1f}% |
| (-) Operating Expenses  | W{operating_expenses:>14,} | {(operating_expenses/revenue*100):>5.1f}% |
| Net Income              | W{net_profit:>14,.0f} | {(net_profit/revenue*100):>5.1f}% |

EXPENSE BREAKDOWN (Estimated)
{'-'*60}
| Category       | Amount           | % of Total |
|----------------|------------------|------------|
| Personnel      | W{expenses*0.43:>14,.0f} | 43%        |
| Marketing      | W{expenses*0.21:>14,.0f} | 21%        |
| Operations     | W{expenses*0.14:>14,.0f} | 14%        |
| Technology     | W{expenses*0.12:>14,.0f} | 12%        |
| Other          | W{expenses*0.10:>14,.0f} | 10%        |

KEY PERFORMANCE INDICATORS
{'-'*60}
| KPI              | Value    | Status |
|------------------|----------|--------|
| Gross Margin     | {(gross_profit/revenue*100):>6.1f}%  | {'OK' if gross_profit/revenue > 0.5 else 'LOW'} |
| Net Margin       | {profit_margin:>6.1f}%  | {'OK' if profit_margin > 20 else 'LOW'} |
| Expense Ratio    | {(expenses/revenue*100):>6.1f}%  | {'OK' if expenses/revenue < 0.4 else 'HIGH'} |

RECOMMENDATIONS
{'-'*60}
"""

    # Add recommendations based on metrics
    recommendations = []
    if profit_margin < 20:
        recommendations.append("1. [PROFIT] Margin below 20% - review pricing strategy")
    if expenses / revenue > 0.4:
        recommendations.append("2. [COST] Expense ratio high - identify cost reduction areas")
    if revenue_growth < 10:
        recommendations.append("3. [GROWTH] Revenue growth below 10% - increase marketing")

    if recommendations:
        report += '\n'.join(recommendations)
    else:
        report += "All metrics within healthy ranges. Continue current strategy."

    report += f"""

{'='*60}
Report Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
{'='*60}
"""

    return report, {
        'period': period,
        'revenue': revenue,
        'expenses': expenses,
        'cogs': cogs,
        'gross_profit': gross_profit,
        'net_profit': net_profit,
        'profit_margin': profit_margin,
        'revenue_growth': revenue_growth,
        'profit_growth': profit_growth
    }

def save_report(report_text, data, output_dir='Output'):
    """Save report to files."""
    os.makedirs(output_dir, exist_ok=True)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

    # Save markdown
    md_path = f"{output_dir}/financial_report_{timestamp}.md"
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(report_text)
    print(f"  Markdown: {md_path}")

    # Save Excel if pandas available
    if PANDAS_AVAILABLE:
        xlsx_path = f"{output_dir}/financial_report_{timestamp}.xlsx"

        # Create multiple sheets
        with pd.ExcelWriter(xlsx_path) as writer:
            # Summary sheet
            summary_df = pd.DataFrame([{
                'Period': data['period'],
                'Revenue': data['revenue'],
                'COGS': data['cogs'],
                'Gross Profit': data['gross_profit'],
                'Operating Expenses': data['expenses'],
                'Net Profit': data['net_profit'],
                'Profit Margin %': data['profit_margin']
            }])
            summary_df.to_excel(writer, sheet_name='Summary', index=False)

            # Expense breakdown
            expense_df = pd.DataFrame([
                {'Category': 'Personnel', 'Amount': data['expenses']*0.43, 'Percentage': 43},
                {'Category': 'Marketing', 'Amount': data['expenses']*0.21, 'Percentage': 21},
                {'Category': 'Operations', 'Amount': data['expenses']*0.14, 'Percentage': 14},
                {'Category': 'Technology', 'Amount': data['expenses']*0.12, 'Percentage': 12},
                {'Category': 'Other', 'Amount': data['expenses']*0.10, 'Percentage': 10},
            ])
            expense_df.to_excel(writer, sheet_name='Expenses', index=False)

        print(f"  Excel: {xlsx_path}")

    # Save JSON
    json_path = f"{output_dir}/financial_report_{timestamp}.json"
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"  JSON: {json_path}")

def main():
    # Default values
    revenue = 100000000  # 1억
    expenses = 40000000  # 4천만
    period = None

    # Parse arguments
    i = 1
    while i < len(sys.argv):
        if sys.argv[i] == '--revenue' and i + 1 < len(sys.argv):
            revenue = float(sys.argv[i + 1])
            i += 2
        elif sys.argv[i] == '--expenses' and i + 1 < len(sys.argv):
            expenses = float(sys.argv[i + 1])
            i += 2
        elif sys.argv[i] == '--period' and i + 1 < len(sys.argv):
            period = sys.argv[i + 1]
            i += 2
        else:
            i += 1

    print("\n[Generating Financial Report...]")
    report_text, data = generate_report(revenue, expenses, period)

    print(report_text)

    print("\n[Saving Files...]")
    save_report(report_text, data)

if __name__ == "__main__":
    main()
