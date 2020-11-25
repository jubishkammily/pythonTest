import http.client

conn = http.client.HTTPSConnection("indianstockexchange.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "f85ff8703fmsh249bf3bcb0df2d9p160b5fjsn6d397c4e4cc1",
    'x-rapidapi-host': "indianstockexchange.p.rapidapi.com"
    }

conn.request("GET", "/index.php?id=null", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))