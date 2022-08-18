import testcase_init
import requests

url = "http://172.16.100.101:8080/cmn/testcase/start?bizId="+str(testcase_init.bizid)+"&dutRuntimeIds="+str(testcase_init.runtimeId)

payload={}
headers = {
  'Content-Type': 'application/x-www-form-urlencoded',
  'Host': '172.16.100.101:8080',
  'Cookie': testcase_init.cookie
}

response = requests.post(url, headers=headers, data=payload)

print(response.text)

