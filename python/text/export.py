import requests

# get your API key https://app.ioannotator.com/api
params= {'apikey': 'add your API key here',
         'dataset': 'add your dataset ID here',}

api = 'https://api.ioannotator.com/export'


x = requests.get(api, params=params)

print(x.text)