# What is Alpha Vantage?
![Build Status](https://travis-ci.org/RomelTorres/alpha_vantage.png?branch=master)
![PyPI version](https://badge.fury.io/py/alpha_vantage.svg)
![Documentation Status](https://readthedocs.org/projects/alpha-vantage/badge/?version=latest)
![Average time to resolve an issue](http://isitmaintained.com/badge/resolution/RomelTorres/alpha_vantage.svg)
![Percentage of issues still open](http://isitmaintained.com/badge/open/RomelTorres/alpha_vantage.svg)
> A fast, lightweight Python interface to the AlphaVantage API

[Alpha Vantage](www.alphavantage.co) offers free realtime financial data and historical market data. This module implements a python interface to the free API provided by Alpha Vantage. This project requires a free API key, which can be found at this [website](www.alphavantage.co). 

---
## Example Usage
```python
from AlphaVantage.client import Client

client = client()
client.get_historical_quote("MSFT", "5min")
```

