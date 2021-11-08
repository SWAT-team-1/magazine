from pandas.core.frame import DataFrame
import requests
from bs4 import BeautifulSoup
import pandas as pd
# Major financial data & indicators for companies listed at ASE

domain = 'https://www.ase.com.jo/en/bulletins/daily/new'


def get_stock_table_report(url):
    """
    get_stock_table_report : web scrapping
    argument : url as a string
    return : scrapped url as Data Frame to be anlayzed or filtered
    """
    # scrapping the domain
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    tables = soup.find_all("table", attrs={"id": "daily-bulletins-table"})
    tableMatrix = []
    for table in tables:
        # turning the scrapped data into matrix to form it as a table
        list_of_rows = []
        for row in table.findAll('tr')[1:]:
            list_of_cells = []
            for cell in row.findAll('td'):
                list_of_cells.append(cell.text)
            list_of_rows.append(list_of_cells)
        tableMatrix.append([list_of_rows, list_of_cells])
    # removing first empty cells and rows
    tableMatrix[0][0].pop(0)
    tableMatrix[0][0].pop(1)
    tableMatrix[0][0].pop(0)
    tableMatrix[0][0].pop(0)
    # cleaning the matrix into list of cloumns in rows
    table_list = []
    for i in range(len(tableMatrix[0][0])):
        if len(tableMatrix[0][0][i]) > 6:
            # structuring the Data Frame
            name = tableMatrix[0][0][i][6]
            symbol = tableMatrix[0][0][i][7]
            lat_closing_price = tableMatrix[0][0][i][9]
            price = tableMatrix[0][0][i][11:15]
            change_price = tableMatrix[0][0][i][15]
            value_traded = tableMatrix[0][0][i][17]
            bid = tableMatrix[0][0][i][19:22]
            table_list.append([name, symbol, lat_closing_price, price[0], price[1],
                              price[2], price[3], change_price, value_traded, bid[0], bid[1], bid[2]])
    # forming the list into DataFrame to be analyzed
    df = pd.DataFrame(table_list, columns=['name', 'symbol', 'last_closing_price', 'opening_price', 'high_price', 'low_price',
                      'closing_price', 'change_price', 'value_traded_jd', 'no_of_trans', 'best_bid_price', 'best_bid_no_of_shares'])
    return df


def get_daily_stock_exchange(df):
    # equasion of percentage
    # percents = []
    # for i in range(len(df.index)):
    #     # change_price = df[int(float('change_price'))][i]
    #     # opening_price = df['opening_price'][i]
    #     df['change_price']
    #     percentage_equagion = (df['change_price'][i].to_numeric()/df['opening_price'][i].to_numeric())*100
    #     percents.append(percentage_equagion)

    # # df["change_price"].to_numeric().replace({percentage_equagion}, inplace=True)
    # percentage = df.set_index('percentage')
    # percentage = '1%'

    # for i in range(len(df.index)):
    #     percentage = int(float(df[['change_price'][i]]))   

    symbol_list = df[['symbol', 'name', 'change_price']].sort_values('change_price', ascending=False)
    print (symbol_list)

    response = input('****** Please enter the Stock symbol for more details (ex: ARBK) or q for quiting > ').strip().title().upper()
    while response != 'Q':
        found=True
        df_selected = df[df['symbol'] == response]
        if len(df.index) > 0:
            found=False            
        print (df_selected)
        break

        if found:  
            print(f" ****** {response} this stock is not found  ******")
        response=input(' ******search for another stock or q for quiting  >').strip().title().upper()
    return

if __name__ == '__main__':

    print('''   
****************************************************************************
******              Welcome to the STOCK MARKET section               ******
****************************************************************************''')

    print(get_daily_stock_exchange(get_stock_table_report(domain)))
    
    
    
