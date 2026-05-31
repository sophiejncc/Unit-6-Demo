import sys
from pathlib import Path

def main():
    test = "test"
    test = "test2"
    base_dir = Path(__file__).parent
    stock_data = read_csv(base_dir / "data/stock_data.csv")
    sales_data = read_csv(base_dir / "data/sales_data.csv")

    merged_data = merge_data(stock_data , sales_data)
    processed_data = update_stock(merged_data)

if __name__ == "__main__":
    sys.exit(main())