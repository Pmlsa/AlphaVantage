from multiprocessing.pool import ThreadPool

API_HOST = 'www.alphavantage.co'
API_KEY = "demo"

INTERVALS = [
    '1min',
    '5min',
    '15min',
    '30min',
    '60min'
]

OUTPUT_SIZE = [
    'compact',
    'full'
]

def ThreadedRequest(symbols, function):
        pool = ThreadPool(len(symbols))
        results = pool.map(function, symbols)
        pool.close()
        pool.join()

        return results
