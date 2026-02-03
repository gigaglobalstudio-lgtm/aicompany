import sys

def calculate(price, cost, shipping):
    try:
        fees = price * 0.05 # Platform fee 5%
        profit = price - cost - shipping - fees
        margin = (profit / price) * 100
        return profit, margin
    except:
        return 0, 0

if __name__ == "__main__":
    # Default values if arguments are missing
    p = float(sys.argv[1]) if len(sys.argv) > 1 else 30000
    c = float(sys.argv[2]) if len(sys.argv) > 2 else 10000
    s = float(sys.argv[3]) if len(sys.argv) > 3 else 3000

    profit, margin = calculate(p, c, s)

    print(f"--- FINANCE REPORT ---")
    print(f"Selling Price: {p} KRW")
    print(f"Sourcing Cost: {c} KRW")
    print(f"Net Profit: {profit:.0f} KRW")
    print(f"Margin Rate: {margin:.2f}%")
