import requests
import csv

# get your API key https://app.ioannotator.com/api
params= {'apikey': 'add your API key here'}
api = 'https://api.ioannotator.com/import/texts'

# sample csv can be found here https://github.com/Io-Annotator/Samples/blob/main/python/text/sample.csv
with open('./sample.csv') as csvfile:
    rows = csv.DictReader(csvfile, delimiter=';')

    for row in rows:

        data = {
                'dataset': '5760835792142336',
                'text': row['text']}

        x = requests.post(api, json = data, params=params)
        print(x)