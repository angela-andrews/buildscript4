#!/usr/bin/env python3

import requests
from requests import Session
import secrets
from pprint import pprint as pp

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/map'
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'secrets.API_KEY'
}


r = requests.get(url, headers=headers)
r.status_code

class CMC:
    def __init__(self, token):
        self.apiurl = 'https://pro-api.coinmarketcap.com'
        self.headers =  {'Accepts': 'application/json','X-CMC_PRO_API_KEY': token}
        self.session = Session()
        self.session.headers.update(self.headers)

    def getAllCoins(self):
        url = self.apiurl + '/v1/cryptocurrency/map'
        r = self.session.get(url)
        data = r.json()['data']
        return data

    def getPrice(self, symbol):
        url = self.apiurl + '/v1/cryptocurrency/quotes/latest'
        parameters = {'symbol': symbol}
        r = self.session.get(url, params=parameters)	
        data = r.json()['data']
        return data


cmc = CMC(secrets.API_KEY)

# pp(cmc.getAllCoins())
pp(cmc.getPrice('BTC'))


# RTFM (https://coinmarketcap.com/api/documentation/v1/#)
# https://pypi.org/project/requests/
# import modues and API key
# test a basic request
# Build up a class so we can easily make the REST API Calls
# export specific data to csv
