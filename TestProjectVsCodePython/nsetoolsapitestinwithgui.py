import tkinter as tk
import json
from nsetools import Nse

window = tk.Tk()

# label = tk.Label(
#     text="Hello, Tkinter",
#     foreground="white",  # Set the text color to white
#     background="black"  # Set the background color to black
# )
# label2 = tk.Label(text="Top Gainers", background="#34A2FE")
# greeting = tk.Label(text="Hello, Tkinter")
#greeting.pack()
#label.pack()
#label2.pack()
# text_box = tk.Text()
# text_box.pack()
#entry = tk.Entry(fg="yellow", bg="blue", width=50)
#entry = tk.Entry()
#entry.pack()





nse = Nse()
top_gainers = nse.get_top_gainers()

y = json.dumps(top_gainers)
json_dictionary = json.loads(y)

#textListString = ""

# for key in json_dictionary:
#     #print(key)
#     j2 = json.dumps(key) 
#     #print(key['symbol']+ ' Open Price :' +str(key['openPrice']))
#     textListString = textListString + key['symbol']+ ' Open Price :' +str(key['openPrice']) + '\n'
    
# label3 = tk.Label(text=textListString, background="#34A2FE")
# label3.pack()



# textListString = ""
# for key in json_dictionary:
#     #print(key)
#     j2 = json.dumps(key) 
#     #print(key['symbol']+ ' Open Price :' +str(key['openPrice']))
#     textListString = textListString + key['symbol']+ ' Open Price :' +str(key['openPrice']) + '\n'
      

# label = tk.Label(text=f"{textListString}")
# label.pack()
res = {}
for val in json_dictionary:
    res[val['symbol']] =  val['openPrice']
    


print(res)



for val2 in res.keys():
    print(val2 + ""+ res[val2])



window.mainloop()




#print(nse)

#q = nse.get_quote('infy') # it's ok to use both upper or lower case for codes.
#from pprint import pprint # just for neatness of display
# pprint(q)

p = nse.get_index_quote("nifty bank") # code can be provided in upper|lower case.

