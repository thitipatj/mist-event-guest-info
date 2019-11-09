import configparser
import requests
import json
import csv
import sys
reload(sys)
sys.setdefaultencoding('utf8')

config = configparser.ConfigParser()
config.read("config.ini")

url = "https://api.mist.com/api/v1/sites/"+config.get('Global_Var', 'SITE')+"/guests"

headers = {
    'Content-Type': "applicantion/json",
    'Authorization': "Token "+config.get('Global_Var', 'TOKEN'),
    'cache-control': "no-cache",
    'Postman-Token': "9db0e494-9517-4dec-9bcd-3fc31f046ef2"
    }

response = requests.request("GET", url, headers=headers)

data = json.loads(response.text)
guest_count=0
dash = '-' * 60
print (dash)
print('{:<35s}{:<25s}'.format("Name:","Email:"))
print (dash)
with open('guest_list.csv', mode='w') as guest_file:
    employee_writer = csv.writer(guest_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    employee_writer.writerow(["Name", "Email"])
    for element in data:
        name = element['name'].encode("utf-8")
        email = element['email']
        print('{:<35s}{:<25s}'.format(name,email))
        guest_count+=1
        employee_writer.writerow([name,email])
print (dash)
print('{:<10s}{:<50d}'.format("Total:",guest_count))
print (dash)
print ("File Write Completed!")
guest_file.close()