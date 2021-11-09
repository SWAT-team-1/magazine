from typing import Type
import pytest
from magazine.stock_market_bot import get_stock_table_report

domain = 'https://www.ase.com.jo/en/bulletins/daily/new'
test_df = get_stock_table_report(domain)

# check number of rows
def test_get_stock_table_report_rows():
    # index = test_df.index    
    actual = len(test_df.index)
    expected = 100
    assert actual == expected

# check if names not null
def test_get_stock_table_report_names_not_null():    
    actual = test_df['name'][0]    
    assert actual

# check if names have string data type (not NONE)
def test_get_stock_table_report_names_type():    
    actual = type(test_df['name'][0])
    expected = str
    assert actual == expected

##########################################################

