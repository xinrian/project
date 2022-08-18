import requests
import json

url = "http://172.16.2.178/api/coupling/powerMeasures/1"

payload = json.dumps({
  "couplingGetPowerParam": {
    "channel": 36,
    "frequency": 5180,
    "compress": 0
  },
  "min": -5,
  "max": 8,
  "loss": 2,
  "count": 1,
  "timeout": 1
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
