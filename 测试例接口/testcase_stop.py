import requests
import testcase_start
import testcase_init
url = "http://172.16.100.101:8080/cmn/testcase/stop?bizId="+ str(testcase_init.bizid)
print(url)
headers = {
  'Content-Type': 'application/x-www-form-urlencoded',
  'Host': '172.16.100.101:8080',
  'Cookie':testcase_init.cookie
}

response = requests.request("POST", url, headers=headers)

print(response.text)
