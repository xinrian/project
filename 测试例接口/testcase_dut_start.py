import testcase_init
import requests
import testcase_start

payload={}
headers = {
  'Content-Type': 'application/x-www-form-urlencoded',
  'Host': '172.16.100.101:8080',
  'Cookie':testcase_init.cookie
}

response = requests.request("POST", testcase_start.url, headers=headers, data=payload)

print(response.text)