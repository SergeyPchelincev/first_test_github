

# import requests
# from bs4 import BeautifulSoup as bs
#
# def download_clk_sp3(url_template):
#
#     req = requests.get(url_template)
#
#     if req.status_code == 200:
#
#         soup = bs(req.text, 'lxml')
#
#         for link in soup:
#             print(link)
#
#
#
#
# if __name__ == '__main__':
#
#
#     url_template = "https://cddis.nasa.gov/archive/gnss/products/"
#
#     download_clk_sp3(url_template)


import requests
url = 'https://cddis.nasa.gov/archive/gnss/products/'
values = {'username': 'vladimirPchelinc',
          'password': '1290112901Qq'}

r = requests.post(url, data=values)

print(r.status_code)
print (r.content)