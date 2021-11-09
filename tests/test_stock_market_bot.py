from typing import Type
import pytest
from magazine.stock_market_bot import get_stock_table_report, get_daily_stock_exchange
import mock

domain = 'https://www.ase.com.jo/en/bulletins/daily/new'
test_df = get_stock_table_report(domain)

# check number of rows
def test_get_stock_table_report_rows():
    # index = test_df.index    
    actual = len(test_df.index)
    expected = 80
    assert actual > expected

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

def test_first_stock_table_report():
    with mock.patch('builtins.input', return_value="1"):
        actual = get_daily_stock_exchange(test_df,'Haneen')
        expected = '''****************************************************************************
    ******                                                                ******
    ******              Welcome to the STOCK MARKET section               ******
    ******                                                                ******
    ****************************************************************************
    ******* MENU ==> Daily Stock Exchange (ASE) (1)
    ******* MENU ==> Top Transactions (2)
    ******* MENU ==> Search for Stock (3)
    Bot: Please choose from the menu or q to quit
    Haneen: '''
    assert actual == expected

def test_filtered_by_stock():
    with mock.patch('builtins.input', return_value="3"):
        expected = 'Bot: Pick the Stock symbol for more details (ex: ARBK) or q for quiting / * for menu'
        actual = get_daily_stock_exchange(test_df,'Haneen')
        assert actual == expected
        
def test_quitting_stock():
    with mock.patch('builtins.input', return_value="q"):
        expected = '************* THANKS FOR VISITING ...! *************'
        actual = get_daily_stock_exchange(test_df,'Haneen')
        assert actual == expected
