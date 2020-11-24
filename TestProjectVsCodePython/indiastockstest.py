import json
from nsetools import Nse
nse = Nse()
print(nse)
top_gainers = nse.get_top_gainers()


y = json.dumps(top_gainers)
json_dictionary = json.loads(y)
print('Top Gainers')

for key in json_dictionary:
    #print(key)
    j2 = json.dumps(key) 
    print(key['symbol']+ ' Open Price :' +str(key['openPrice']))
    # j3 = json.loads(j2)  
    #print(j3['symbol'])    