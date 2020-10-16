import requests

# get your API key https://app.ioannotator.com/api
params= {'apikey': 'add your API key here'}
api = 'https://api.ioannotator.com/import/texts'

data = {
        'dataset': 'add your dataset ID here',
        'text': 'the text you want to annotate'}

x = requests.post(api, json = data, params=params)

print(x)