

from pydoh import yahoo

symbol = 'FDS'
params = None
interval = '1wk'
periodocity = '1mo'
period1 = 1641059569
period2 = 1641579977

data = yahoo.call(symbol, interval, periodocity, params)

for r in data['result']:
    print('SYMBOL:', r['meta']['symbol'], r['meta']['currency'], r['meta']['exchangeName'], r['meta']['firstTradeDate'])
    print('INDICATORS:', r['indicators'].keys())
    for k,v in r['indicators'].items():
        print(k, 'class:', v.__class__.__name__)
        for x in v:
            for k2,v2 in x.items():
                print('  ', k2,v2)

print('Done')

