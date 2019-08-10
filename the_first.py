import requests
url = 'https://vk.com/id514908092'
json = {
    'month' : 'May',
    'day' : '09'
}

response = requests.post(url,json=json)
print(response.text)
print(response.status_code)
print(response.url)


