import requests
import json
#url = "https://www.tistory.com/apis/post/write?access_token=e5c6a055ee27506ffa96947262aa791d_17046ffb71364dceb0565ffd5e464348"
url = "https://www.tistory.com/apis/post/list?access_token=e5c6a055ee27506ffa96947262aa791d_17046ffb71364dceb0565ffd5e464348"
get_data = {
    'blogName': 'revoltoso',
    'title': 'hi',
    'content': 'test1',
}
post_data = {
    'blogName': 'revoltoso',
    'page' : 1,
    'output' : 'json'
}

headers = {"Content-Type": "application/x-www-form-urlencoded"}

#response = requests.request(
#    "POST", url, headers=headers, data=post_data)

#response = requests.request(
#    "GET", url, headers=headers, params=post_data)

response = requests.get(url, params=post_data)

print(response.url)
print(response.text)
