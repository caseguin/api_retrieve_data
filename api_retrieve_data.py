import requests

ng_url = 'https://www.newegg.ca/p/pl?d=4070&N=601408877%20100007708'

response = requests.get(ng_url)

print(response.status_code)
print(response.json())