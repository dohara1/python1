################
# yahoo module #
################

import requests

# https://cryptocointracker.com/yahoo-finance/yahoo-finance-api

user_agent = 'Mozilla/5.0'
user_agent = 'python-requests'

#modules = 'financeData'  # csv
#url = f'https://query1.finance.yahoo.com/v10/finance/quoteSummary/{symbol}?modules={modules}'


module = 'chart'

url_mask = 'https://query1.finance.yahoo.com/v8/finance/{module}/{symbol}?interval={interval}&range={periodocity}'

"""
module = 'download'
interval = '1wk'
period1 = 1641059569
period2 = 1641579977
url = f'https://query1.finance.yahoo.com/v7/finance/download/{symbol}?interval={interval}&period1={period1}&period2={period2}'
"""

#??
#params = { 'symbols':'FDS', 'interval':'1wk', 'range':'1mo' }

def call(symbol, interval, periodocity, params):
    print(url_mask)
    url = url_mask.format(module=module, symbol=symbol, interval=interval, periodocity=periodocity)
    print('URL:', url)

    if params is None:
        resp = requests.get(url, headers={'User-agent': user_agent})
    else:
        resp = requests.get(url, headers={'User-agent': user_agent}, params=params)

    print(resp.status_code, resp.reason)
    if resp.status_code == 200:
        if module == 'download':
            print(resp.text)
        else:
            data = resp.json()[module]
            print(data.keys())
            print('ERROR:', data['error'])
            print(data['result'][0].keys())
            print('META[0]:', data['result'][0]['meta'])
    return data
