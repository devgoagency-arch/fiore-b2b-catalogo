import urllib.request, json, base64

url = 'https://fiorefoodscanada.com/wp-json/wc/v3/products?per_page=100&page=1&status=publish'
auth = b'ck_4bf4758557b77ab46cf6791e2b5b31df1240c5f2:cs_775a2283e33e49dfcf56cdfa3369be36e1cdaab2'
headers = {
    'Authorization': 'Basic ' + base64.b64encode(auth).decode('utf-8'),
    'User-Agent': 'Mozilla/5.0'
}

req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req) as response:
    data = json.loads(response.read().decode())
    p = next((x for x in data if 'Don Jose Sliced Jamon Iberico Bellota' in x['name']), None)
    if p:
        print(p['description'])
    else:
        print('Not found on page 1')
