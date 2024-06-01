import requests

url = 'http://127.0.0.1:5000/add_user'
data = {
    'username': 'anibal',
    'name': 'anibal',
    'age': 29,
    'city': 'Puerto Rico'
}

response = requests.post(url, json=data)

print(response.status_code)
print(response.json())
