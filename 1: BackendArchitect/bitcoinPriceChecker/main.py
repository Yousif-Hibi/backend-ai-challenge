from bitcoin_value import currency
import requests
from coinpaprika.client import Client
import json
import requests


def price2():
    url = 'https://api.coingecko.com/api/v3/simple/price'
    params = {  
            'ids': 'bitcoin',
            'vs_currencies': 'USD'
    }

    response = requests.get(url, params = params) 
    if response.status_code == 200:
            data = response.json()
            Bitcoin_price = data['bitcoin']['usd']
            return Bitcoin_price
    else:
            print('Failed to retrieve data from the API')



def price3():
    free_client = Client()
    rdict = free_client.price_converter(base_currency_id="btc-bitcoin", quote_currency_id="usd-us-dollars", amount=1)
    return rdict['price']


def price4():
    key = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"

    # requesting data from url
    data = requests.get(key)  
    data = data.json()
    return data['price']
def price5():
    key = "https://api-pub.bitfinex.com/v2/ticker/tBTCUSD"

    # requesting data from url
    data = requests.get(key)  
    data = data.json()
    return data[0]

def price1():
    key = "https://api.blockchain.info/stats"

    # requesting data from url
    data = requests.get(key)  
    data = data.json()
    return data['market_price_usd']
def main() :    
    p5 = int(float(price5()))
    p4 = int(float(price4()))
    p3 = int(float(price3()))
    p2 = int(float(price2()))
    p1 = int(float(price1()))
    total = (p1+p2+p3+p4+p5)/5
    print(f"current bitcoin price {total}.")

if __name__ == "__main__":
    main()