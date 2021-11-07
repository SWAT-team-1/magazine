import requests
from bs4 import BeautifulSoup
import pandas as pd
# Major financial data & indicators for companies listed at ASE

domain = 'https://www.ase.com.jo/en/bulletins/daily/new'


def get_stock_table(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    result = soup.find("table", attrs={"id": "daily-bulletins-table"})
    return (result.prettify())

# print(get_stock_table(domain))


def get_excel_dounloader(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    tables = soup.find_all("table", attrs={"id": "daily-bulletins-table"})
    tableMatrix = []
    for table in tables:
        # Here you can do whatever you want with the data! You can findAll table row headers, etc...
        list_of_rows = []
        for row in table.findAll('tr')[1:]:
            list_of_cells = []
            for cell in row.findAll('td'):
                list_of_cells.append(cell.text)
            list_of_rows.append(list_of_cells)
        tableMatrix.append([list_of_rows, list_of_cells])
        
    tableMatrix[0][0].pop(0)
    tableMatrix[0][0].pop(1)
    tableMatrix[0][0].pop(0)
    tableMatrix[0][0].pop(0)

    table_list = []
    for i in range(len(tableMatrix[0][0])):
        if len(tableMatrix[0][0][i]) > 6:
            name = tableMatrix[0][0][i][6]
            lat_closing_price = tableMatrix[0][0][i][9]
            price = tableMatrix[0][0][i][11:15]
            value_traded = tableMatrix[0][0][i][17]
            bid = tableMatrix[0][0][i][19:22]

            table_list.append([name,lat_closing_price,price[0],price[1],price[2],price[3],value_traded,bid[0],bid[1],bid[2]])
    df = pd.DataFrame(table_list, columns=['name', 'last_closing_price', 'opening_price', 'high_price', 'low_price','closing_price','value_traded_jd','no_of_trans', 'best_bid_price', 'best_bid_no_of_shares'])
    return df


print(get_excel_dounloader(domain))


def get_stock_table_report(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    result = soup.find_all('td', class_='odd')
    td = []
    link = f"{domain}{soup[0].find('a').get('href')}"
    for td in result:
        td.append(td.text.strip())
    return '\n'.join(td)


# print(get_stock_table_count(domain))

# df = pd.DataFrame(data=numpy_data, index=["row1", "row2"], columns=["column1", "column2"])
