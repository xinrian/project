import requests
import json

url = "http://172.16.100.101:8080/cmn/testcase/init?name=test"
cookie = 'ck=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJyb290IiwiaWF0IjoxNjU4OTI2MjczLCJleHAiOjE2NTkwOTkwNzN9.ZsJJwHgVzwJrLLSkl8WhAU7Ek9P2aYX81Lr3Av2GNqwQtK2Qt_v9gPuF2QrCbGsRnvkFF4wiTI88n0rpvfiaZg; ck=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJyb290IiwiaWF0IjoxNjU4OTc1NTI1LCJleHAiOjE2NTkxNDgzMjV9.mqEOcnYnqIwQOZwG8Knq2wOALssO14gC0CKgnyL9dJYLBz3xxOmwhfbTMOCRruKioWAGfF2Z44IfyuqV_xpVuw'

payload={}
files={}
headers = {
  'Cookie': cookie,
  'Host': '172.16.100.101:8080'
}

response = requests.request("GET", url, headers=headers, data=payload, files=files)

result = json.loads(response.text)

bizid = result.get('result').get('bizId')

runtimeId = result.get('result').get("duts")[0].get('runtimeId')

print(bizid)
print(runtimeId)


