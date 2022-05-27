'''
IMPORTS
'''
import requests
import json
from config import keys

from model.driver import predict_high

'''
ALL FUNCTIONS BELOW ARE TO FETCH DATA FROM THE WEB AND SAVE IT TO A JSON FILE
'''

def company_details(ticker: str):
    """
    Get the company details from the web.
    """
    url = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol=' + ticker + '&apikey=' + keys['alpha_vantage_key']
    response = requests.get(url)
    return response.json()

def search(stock_name: str):
    """
    Get the ticker from the web.
    """
    url = 'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords=' + stock_name + '&apikey=' + keys['alpha_vantage_key']
    response = requests.get(url)
    return response.json()

def fetchDaily(ticker: str):
    """
    Fetch daily data from the web.
    """
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=' + ticker + '&outputsize=full&apikey=' + keys['alpha_vantage_key']
    response = requests.get(url)
    return response.json()

def fetchIntraDay(ticker: str):
    """
    Fetch intra day data from the web.
    """
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=' + ticker + '&interval=5min&outputsize=full&apikey=' + keys['alpha_vantage_key']
    response = requests.get(url)
    return response.json()

def saveByDay(stock_name: str):
    """
    Get the output by day from the web.
    """
    with open('data/' + stock_name + '-stocks.json', 'w') as f:
        json.dump(fetchDaily(search(stock_name)['bestMatches'][0]['1. symbol']), f)

def saveByIntraDay(stock_name: str):
    """
    Get the output by intra day from the web.
    """
    with open('data/' + stock_name + '-stocks.json', 'w') as f:
        json.dump(fetchIntraDay(search(stock_name)['bestMatches'][0]['1. symbol']), f)


'''
Testings
'''


#print(fetch('MSFT'))

#saveByDay('Microsoft')
'''
print(company_details('MSFT'))
print('\nPrediction for next day:', predict_high(fetchDaily('MSFT'), 1))
'''

'''
with open('stocks.json', 'w') as f:
    json.dump(fetch('MSFT'), f)
'''