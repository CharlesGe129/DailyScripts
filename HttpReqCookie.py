import requests

url = "http://localhost:2050/hotelInfo?hotelId=10323"

cookies = {"login": "true"}

r = requests.get(url, cookies=cookies)
print(r.text)

