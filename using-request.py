import requests

url= 'https:///www.google.com'
response = requests.get(url)
response(f'Response returned: {resonse.status_code}, {response.reason}')
print(response.text[:200])
