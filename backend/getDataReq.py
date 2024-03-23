import requests
import json
# Use your own API key here
def stockInf(symbol):
    apikey = ""  #please input your alphavantage api key they are free to sign up for
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&outputsize=full&apikey={apikey}'

    r = requests.get(url)
    data = r.json()


    return data

