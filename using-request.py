import requests

url = 'https:///www.google.com'
response = requests.get(url)
response(f'Response returned: {response.status_code}, {response.reason}')
print(response.text[:200])
