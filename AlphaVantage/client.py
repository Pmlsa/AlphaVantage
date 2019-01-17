import json
import urllib3
from urllib3 import HTTPSConnectionPool
from multiprocessing.pool import ThreadPool

urllib3.disable_warnings()

from util import (
    API_KEY, 
    API_HOST, 
    INTERVALS, 
    OUTPUT_SIZE,
    ThreadedRequest
)

class Client:
    '''
    A fast, lightweight Python interface to the AlphaVantage API

    Usage:
        client = Client()
        client.get_quote("MSFT")

    '''

    def __init__(self):
        self.session = HTTPSConnectionPool(API_HOST)
        self.ThreadedRequest = ThreadedRequest

    def get_quote(self, symbol):
        '''
        fetch realtime quote for a stock

        :param symbol: a stock symbol
        :returns: realtime quote of the given symbol in json format

        '''

        payload = {
            "function" : "GLOBAL_QUOTE", 
            "symbol" : symbol, 
            "apikey" : API_KEY
        }
        r = self.session.request('GET',  '/query', fields=payload)
        return json.loads(r.data)

    def get_quotes(self, symbols):
        '''
        threaded request for fetching multiple realtime stock quotes

        :param symbols: a list of stock symbols
        :returns: list of stock quotes in json format

        '''

        results = ThreadedRequest(symbols, self.get_quote)

        return results

    def get_historical_quote(self, symbol, interval, output_size = "full"):
        '''
        fetch historical data for a stock

        :param symbol: a stock symbol
        :param interval: aggragated time period for historical data (1min, 5min, 15min, 30min, 60min)
        :param output_size: ammount of data returned (full, compact)
        :returns: a list of historical stock quotes in json format

        '''

        assert interval in INTERVALS
        assert output_size in OUTPUT_SIZE

        payload = {
            "function" : "TIME_SERIES_INTRADAY", 
            "symbol" : symbol, 
            "interval" : interval, 
            "outputsize" : output_size, 
            "apikey" : API_KEY
        }

        r = self.session.request('GET',  '/query', fields=payload)
        return json.loads(r.data)

    def get_historical_quotes(self, symbols, interval, output_size = "full"):
        '''
        threaded request for fetching multiple historical stock quotes

        :param symbols: a list of stock symbols
        :param interval: aggragated time period for historical data (1min, 5min, 15min, 30min, 60min)
        :param output_size: ammount of data returned (full, compact)
        :returns: a list of multiple historical stock quotes in json format

        '''

        results = ThreadedRequest(symbols, lambda symbol: self.get_historical_quote(symbol, interval, output_size))

        return results

    def get_sector_preformances(self):
        '''
        fetch realtime sector preformance
        
        :returns: list of sector preformances in json format

        '''

        payload = {
            "function" : "SECTOR", 
            "apikey" : API_KEY
        }

        r = self.session.request('GET',  '/query', fields=payload)
        return json.loads(r.data)
