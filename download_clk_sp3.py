
import requests
url = 'https://cddis.nasa.gov/archive/gnss/products/'
values = {'username': 'vladimirPchelinc',
          'password': '1290112901Qq'}

r = requests.post(url, data=values)

print(r.status_code)
print (r.content)