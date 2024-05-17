import requests
import pprint

response = requests.get('https://api.github.com')
print(response.status_code)
if response.ok:
    print("success")
else:
    print(response.text)

print(response.text)
response_json = response.json()
pprint.pprint(response_json)

