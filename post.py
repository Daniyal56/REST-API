import json
import requests
import pandas as pd

jsonFile = open('names.json', 'r')
jsonData = jsonFile.read()
data = json.loads(jsonData)
i = 0
for x in data['items']:
    r = requests.post(
        'http://151.80.237.86:1251/ords/demo7/zkt/zkt_att', json=x)
    i += 1

