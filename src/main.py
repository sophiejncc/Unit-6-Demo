from helpers import read_data, merge_lists_by_first_column, update_stock_data, check_stock_level, write_data, combine_data

def main():
    stock_data = read_data('src/data/stock_data.csv')
    sales_data = read_data('src/data/sales_data.csv')
    merged_data = merge_lists_by_first_column(stock_data, sales_data)
    new_stock_data = update_stock_data(merged_data)
    check_stock_level(new_stock_data)
    #print(stock_data[1], new_stock_data[1])
    #for item in new_stock_data:
    #    print(item[0])
    combined_data = combine_data(stock_data, new_stock_data)
    print(combined_data)
    write_data(combined_data)

if __name__ == "__main__":
    main()