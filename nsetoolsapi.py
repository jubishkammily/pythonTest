import json
from nsetools import Nse
nse = Nse()
print(nse)

q = nse.get_quote('infy') # it's ok to use both upper or lower case for codes.
from pprint import pprint # just for neatness of display
# pprint(q)

p = nse.get_index_quote("nifty bank") # code can be provided in upper|lower case.

# pprint(p)


top_gainers = nse.get_top_gainers()

#print(top_gainers)
# pprint(top_gainers)

#data = json.load(top_gainers)

# for (k, v) in top_gainers.items():
#    print("Key: " + k)
#    print("Value: " + str(v))

# for key, value in enumerate(top_gainers): 
#     print(value) 
#     break

# for i in top_gainers:
#     print(i.symbol)

y = json.dumps(top_gainers)
json_dictionary = json.loads(y)
print('Top Gainers')

for key in json_dictionary:
    #print(key)
    j2 = json.dumps(key) 
    print(key['symbol']+ ' Open Price :' +str(key['openPrice']))
    # j3 = json.loads(j2)  
    #print(j3['symbol'])     
    



# def get_all_values(nested_dictionary):
#     for key, value in nested_dictionary.items():
#         if type(value) is dict:
#             get_all_values(value)            
#         else:
#             print(key, ":", value)


#get_all_values(top_gainers)