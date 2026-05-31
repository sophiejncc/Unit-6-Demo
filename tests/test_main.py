import csv
import os
import pytest

from helpers import read_data, merge_lists_by_first_column, update_stock_data

@pytest.fixture(scope="module")
def stock_file():
    with open('stock_data.csv', 'w', newline='') as stock_file:
        fieldnames = ['product_id', 'manufacturer_name', 'quantity_in_stock', 'supplier_contact',
                      'last_stock_update', 'price_per_unit', 'category', 'location_in_warehouse', 'reorder_threshold']
        stock_writer = csv.DictWriter(stock_file, fieldnames=fieldnames)
        stock_writer.writeheader()
        stock_writer.writerow({'product_id' : '123', 'manufacturer_name' : 'TestCompany','quantity_in_stock' : "10",
                               'supplier_contact' : '123-456-7891', 'last_stock_update' : '01/01/2000',
                               'price_per_unit': '100.00', 'category' : 'Test', 'location_in_warehouse' : 'A1', 
                               'reorder_threshold': '1'})
    yield
    os.remove('stock_data.csv')

@pytest.fixture(scope="module")
def sales_file():
    with open('sales_data.csv', 'w', newline='') as sales_file:
        fieldnames = ['product_id', 'sales', 'date']
        sales_writer = csv.DictWriter(sales_file, fieldnames=fieldnames)
        sales_writer.writeheader()
        sales_writer.writerow({'product_id': '123', 'sales': '5', 'date': '01/01/2000'})
    yield
    os.remove('sales_data.csv')

def test_read_stock_data(stock_file):
    stock_data = read_data('stock_data.csv')
    assert len(stock_data) == 2
    assert stock_data[1][0] == 123
    assert stock_data[1][2] == 10

def test_read_sales_data(sales_file):
    sales_data = read_data('sales_data.csv')
    assert len(sales_data) == 2
    assert sales_data[1][0] == 123
    assert sales_data[1][1] == 5

def test_update_stock_data(stock_file, sales_file):
    stock_data = read_data('stock_data.csv')
    sales_data = read_data('sales_data.csv')
    stock_data = update_stock_data(merge_lists_by_first_column(stock_data, sales_data))
    assert stock_data[1][2] == 5