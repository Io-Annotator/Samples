import requests
import csv

# get your API key https://app.ioannotator.com/api
params= {'apikey': '8D6F0ES-XXYM6BW-K0JJGBP-G1CCQRY'}
api = 'http://localhost:8080/import/texts'

with open('./sample.csv') as csvfile:
    rows = csv.DictReader(csvfile, delimiter=';')

    for row in rows:

        data = {
                'dataset': '5760835792142336',
                'text': row['text']}

        x = requests.post(api, json = data, params=params)
        print(x)