import requests

def Binify(request_type,payload):
    if request_type == 'get':
        req = requests.get('https://httpbin.org/get', params=payload)
        return req.text
    elif request_type == 'post':
        req = requests.post('http://httpbin.org/post', data=payload)
        return req.text

payload = {
    'page' : 2,
    'count' : 25
}
r = requests.get('https://httpbin.org/get',params= payload)
print('The Get request URL: ', r.url)

payload = {
    'username' : 'Pablo',
    'pasword' : 'Martinez'
}
# Using a post method
r = requests.post('https://httpbin.org/post', data= payload)
print('The Post dictionary: ')
print('\n')

# Using the json method creates a dictionary from the text response by httpbin
print(r.json())
