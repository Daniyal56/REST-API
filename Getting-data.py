import requests
import json
import datetime
import os

url2 = 'http://151.80.237.86:1251/ords/demo7/zkt/zkt_att'
# url = 'https://www.indus-erp.com/ords/indus_iot3/indus_iot3/indus_iot3'

# sending request to get the data from the url
api = requests.get(url)

# check status
# print(api.status_code)

# get data in json format from the URL
text = api.json()
# print(type(text))
# print(text['items'])

# Getting date in UTC Format
date = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'

# #  = [{'userid': int(14), 'checktime': date, 'checktype': 'O'}]

# data = {
#     "userid": '20',
#     # "checktime": os.system('date'),
#     "checktype": "O"}


# payload = [{x, y} for x, y in data.items()]
# json_data = json.dumps(data)
# print(type(json_data))
# print(json_data)

# payload = list(payload)
# y = [{key, value} for key, value in payload.items()]
# print(y)
# print(y)
# print(type(y))

# # print(param)
# print(payload)
# r = requests.post('http://151.80.237.86:1251/ords/demo7/zkt/zkt_att',
#                   data=data)
# print(r.text)
# print(payload)
# print(r.text)
# r = requests.post('')
# data={'userid': 16, 'checktime': datetime.datetime.now(), 'checktype': 'O'})
# # (userid, checktime, checktype
# print(r)

# r = requests.get('https://'+url)

# payload = dict(MCHDB_PK=int(43918), USERID=2925, SENSORID='1', CHECKTYPE='IN',
#                VERIFYCODE='01')/

# payload = dict(userid=54, checktype="O", mchdb_pk=34,
#                sensorid=str(34), verifycode=34, checktime=date)

# data = {'userid': row[0], 'checktype': row[5], 'verifycode': '65'}
# # print(row[0])
# r = requests.post(
#     'http://151.80.237.86:1251/ords/demo7/zkt/zkt_att', json=data)

