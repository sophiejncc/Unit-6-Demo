import csv

def read_data(filename):
    with open(filename, 'r') as file:
        data_reader = csv.reader(file)
        data = [[int(item) if item.isnumeric() else item for item in row] for row in data_reader]
    return data

def merge_lists_by_first_column(list1, list2):
    merged_list = []
    for item1 in list1:
        for item2 in list2:
            if item1[0] == item2[0]:
                merged_list.append(item1 + item2[1:])
                break
    return merged_list

def update_stock_data(merged_data):
    for item in merged_data[1:]:
        item[2] = int(item[2]) - int(item[-2])
    return merged_data


def check_stock_level(data):
    #date = item[10].replace('/','_')
    with open(f'src/data/reorder.csv', 'w+', newline='') as reorder_file:
        fieldnames = ['product_id', 'date']
        reorder_writer = csv.DictWriter(reorder_file, fieldnames=fieldnames)
        reorder_writer.writeheader()
        for item in data[1:]:
            if item[2] < 0: 
                print(f'Product {item[0]} is out of stock.')
                reorder_writer.writerow({'product_id' : item[0], 'date' : item[10]})
        
def combine_data(list1, list2):
    combined_list = []
    
    for item1 in list1:
        in_list = False
        for item2 in list2:
            if item1[0] == item2[0]:
                combined_list.append(item2)
                in_list=True
                break
        if in_list == False:
            combined_list.append(item1)
            
    return combined_list
        
def write_data(data):
    date = data[1][-1].replace('/','_')
    with open(f'src/data/stock_data_{date}.csv', 'w+', newline='') as stock_file:
        fieldnames = ['product_id', 'manufacturer_name', 'quantity_in_stock', 'supplier_contact',
                      'last_stock_update', 'price_per_unit', 'category', 'location_in_warehouse', 'reorder_threshold']
        stock_writer = csv.DictWriter(stock_file, fieldnames=fieldnames)
        stock_writer.writeheader()
        for item in data[1:]:
            stock_writer.writerow({'product_id' : item[0], 'manufacturer_name' : item[1],'quantity_in_stock' : item[2],
                                   'supplier_contact' : item[3], 'last_stock_update' : item[4],
                                   'price_per_unit': item[5], 'category' : item[6], 'location_in_warehouse' : item[7], 
                                   'reorder_threshold': item[8]})