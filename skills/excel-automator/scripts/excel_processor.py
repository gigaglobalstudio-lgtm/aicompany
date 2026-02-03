"""
Excel Automator - Pandas-based Excel processor
Usage: python excel_processor.py [command] [args]

Commands:
  analyze [file]           - Analyze Excel file
  merge [file1] [file2]    - Merge Excel files
  pivot [file] [values] [index] [columns] - Create pivot table
  clean [file]             - Clean data (remove duplicates, handle nulls)
  convert [file] [format]  - Convert between formats (csv, xlsx, json)
"""

import sys
import os
from datetime import datetime

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

try:
    import pandas as pd
    PANDAS_AVAILABLE = True
except ImportError:
    PANDAS_AVAILABLE = False
    print("Error: pandas not installed. Run: pip install pandas openpyxl")

def analyze_excel(file_path):
    """Analyze Excel file and show summary."""
    print(f"\n{'='*60}")
    print(f"Excel Analysis: {os.path.basename(file_path)}")
    print('='*60)

    df = pd.read_excel(file_path)

    print(f"\n[Basic Info]")
    print(f"  Rows: {len(df):,}")
    print(f"  Columns: {len(df.columns)}")
    print(f"  Memory: {df.memory_usage(deep=True).sum() / 1024:.1f} KB")

    print(f"\n[Columns]")
    for col in df.columns:
        dtype = df[col].dtype
        nulls = df[col].isnull().sum()
        print(f"  - {col}: {dtype} (nulls: {nulls})")

    print(f"\n[Statistics]")
    print(df.describe().to_string())

    print(f"\n[First 5 Rows]")
    print(df.head().to_string())

    return df

def merge_excel(file1, file2, output=None):
    """Merge two Excel files."""
    print(f"\n{'='*60}")
    print("Merging Excel Files")
    print('='*60)

    df1 = pd.read_excel(file1)
    df2 = pd.read_excel(file2)

    print(f"  File 1: {len(df1):,} rows")
    print(f"  File 2: {len(df2):,} rows")

    # Vertical merge (append)
    merged = pd.concat([df1, df2], ignore_index=True)

    if output is None:
        output = f"Output/merged_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"

    os.makedirs(os.path.dirname(output) if os.path.dirname(output) else 'Output', exist_ok=True)
    merged.to_excel(output, index=False)

    print(f"\n  Merged: {len(merged):,} rows")
    print(f"  Saved: {output}")

    return merged

def create_pivot(file_path, values, index, columns, output=None):
    """Create pivot table."""
    print(f"\n{'='*60}")
    print("Creating Pivot Table")
    print('='*60)

    df = pd.read_excel(file_path)

    pivot = pd.pivot_table(
        df,
        values=values,
        index=index,
        columns=columns,
        aggfunc='sum',
        fill_value=0
    )

    print(f"\n[Pivot Table]")
    print(pivot.to_string())

    if output is None:
        output = f"Output/pivot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"

    os.makedirs(os.path.dirname(output) if os.path.dirname(output) else 'Output', exist_ok=True)
    pivot.to_excel(output)

    print(f"\n  Saved: {output}")

    return pivot

def clean_data(file_path, output=None):
    """Clean data: remove duplicates, handle nulls."""
    print(f"\n{'='*60}")
    print("Cleaning Data")
    print('='*60)

    df = pd.read_excel(file_path)
    original_rows = len(df)

    # Remove duplicates
    df = df.drop_duplicates()
    after_dedup = len(df)

    # Show null counts
    null_counts = df.isnull().sum()
    print(f"\n[Null Values]")
    for col, count in null_counts.items():
        if count > 0:
            print(f"  {col}: {count}")

    # Fill numeric nulls with 0, string nulls with ''
    for col in df.columns:
        if df[col].dtype in ['int64', 'float64']:
            df[col] = df[col].fillna(0)
        else:
            df[col] = df[col].fillna('')

    print(f"\n[Results]")
    print(f"  Original rows: {original_rows:,}")
    print(f"  Duplicates removed: {original_rows - after_dedup:,}")
    print(f"  Final rows: {len(df):,}")

    if output is None:
        output = f"Output/cleaned_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"

    os.makedirs(os.path.dirname(output) if os.path.dirname(output) else 'Output', exist_ok=True)
    df.to_excel(output, index=False)

    print(f"  Saved: {output}")

    return df

def convert_format(file_path, target_format, output=None):
    """Convert between file formats."""
    print(f"\n{'='*60}")
    print(f"Converting to {target_format.upper()}")
    print('='*60)

    # Read input
    if file_path.endswith('.csv'):
        df = pd.read_csv(file_path)
    elif file_path.endswith('.json'):
        df = pd.read_json(file_path)
    else:
        df = pd.read_excel(file_path)

    # Generate output path
    base_name = os.path.splitext(os.path.basename(file_path))[0]
    if output is None:
        output = f"Output/{base_name}.{target_format}"

    os.makedirs(os.path.dirname(output) if os.path.dirname(output) else 'Output', exist_ok=True)

    # Save in target format
    if target_format == 'csv':
        df.to_csv(output, index=False)
    elif target_format == 'json':
        df.to_json(output, orient='records', force_ascii=False, indent=2)
    elif target_format in ['xlsx', 'excel']:
        df.to_excel(output.replace('.excel', '.xlsx'), index=False)

    print(f"  Input: {file_path}")
    print(f"  Output: {output}")
    print(f"  Rows: {len(df):,}")

    return df

def create_sample_data():
    """Create sample Excel file for testing."""
    print("\n[Creating Sample Data]")

    data = {
        'Date': pd.date_range('2024-01-01', periods=10, freq='D'),
        'Product': ['A', 'B', 'A', 'C', 'B', 'A', 'C', 'B', 'A', 'C'],
        'Category': ['Electronics', 'Clothing', 'Electronics', 'Food', 'Clothing',
                    'Electronics', 'Food', 'Clothing', 'Electronics', 'Food'],
        'Sales': [1000, 2000, 1500, 800, 2200, 1800, 900, 2100, 1600, 750],
        'Quantity': [10, 20, 15, 40, 22, 18, 45, 21, 16, 38]
    }

    df = pd.DataFrame(data)
    output = 'Output/sample_data.xlsx'
    os.makedirs('Output', exist_ok=True)
    df.to_excel(output, index=False)

    print(f"  Created: {output}")
    return df

def main():
    if not PANDAS_AVAILABLE:
        sys.exit(1)

    if len(sys.argv) < 2:
        print(__doc__)
        print("\nCreating sample data for testing...")
        create_sample_data()
        sys.exit(0)

    command = sys.argv[1].lower()

    if command == 'analyze' and len(sys.argv) >= 3:
        analyze_excel(sys.argv[2])

    elif command == 'merge' and len(sys.argv) >= 4:
        output = sys.argv[4] if len(sys.argv) > 4 else None
        merge_excel(sys.argv[2], sys.argv[3], output)

    elif command == 'pivot' and len(sys.argv) >= 6:
        output = sys.argv[6] if len(sys.argv) > 6 else None
        create_pivot(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], output)

    elif command == 'clean' and len(sys.argv) >= 3:
        output = sys.argv[3] if len(sys.argv) > 3 else None
        clean_data(sys.argv[2], output)

    elif command == 'convert' and len(sys.argv) >= 4:
        output = sys.argv[4] if len(sys.argv) > 4 else None
        convert_format(sys.argv[2], sys.argv[3], output)

    elif command == 'sample':
        create_sample_data()

    else:
        print(__doc__)

if __name__ == "__main__":
    main()
