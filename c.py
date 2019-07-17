import requests
import json
import pyexcel

ENDPOINT = 'http://api.open-notify.org/astros.json'

resp = requests.get(ENDPOINT)
dt = resp.json()
print(dt)
my_data = []
for item in my_data:
    my_data.append[item["people"]]


print(my_data)
pyexcel.save_as(records=my_data,dest_file_name="test.xls")
