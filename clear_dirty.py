from requests.auth import HTTPBasicAuth
import json
import requests

url = "https://ucp-sh01:8089/servicesNS/nobody/splunk_app_perf_automation/storage/collections/data/test_jobs/"
user = "admin"
password = "Passw0rd"

response = requests.get(url,auth=HTTPBasicAuth(user,password),verify=0)
content = response.content
with open("backup.json","w") as f:
    f.write(content)
f.close()

datas = json.loads(content)

#dirty_data = [data for data in datas if data.has_key("testJobSummary") and data["testJobSummary"] == {}]
no_summary = [data for data in datas if data.has_key("testJobSummary") == False]
#print dirty_data
#print len(dirty_data)
print len(no_summary)
print len(datas)

# delete_keys = [ elem["_key"] for elem in no_summary]
# print delete_keys

# total = len(delete_keys)
# success_count = 0
# for key in delete_keys:
#     response = requests.delete(url+key,auth=HTTPBasicAuth(user,password),verify=0)
#     if(response.status_code == 200):
#         success_count+=1
# print (success_count + "/" + total)







