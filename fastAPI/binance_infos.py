import os
from binance.client import Client

# A modifier avec variables d'env
api_key = os.environ.get('binance_api')
api_secret = os.environ.get('binance_secret')
client = Client(api_key, api_secret)

def get_infos():
    return [[crypto['asset'],float(crypto['locked']) + float(crypto['free'])] for crypto in client.get_account()['balances'] if float(crypto['free']) > 0] 

