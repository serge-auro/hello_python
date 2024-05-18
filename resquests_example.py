import requests
import pprint

params = {
    'q' : 'html'
}

# if response.ok:
#     print("success")
# else:
#     print(response.text)

#test get request
# response = requests.get('https://api.github.com/search/repositories', params=params)
# response_json = response.json()
# pprint.pprint(response_json)
# print(f"total count={response_json['total_count']}")

#test get request GET userId
# response = requests.get('https://jsonplaceholder.typicode.com/posts', params={'userId': '1'})
# print(response.status_code)
# response_json = response.json()
# pprint.pprint(response_json)

#test img save request
# img = "https://sun1-14.userapi.com/impg/qju-DE6KZ-q_ZQkznTZpRmVSDU4JL-kD6PD9SA/8--DBzGN-WY.jpg?size=1200x800&quality=95&sign=59229db73961503ade563d00a36a925d&type=album"
# response = requests.get(img)
# with open("test.jpg", "wb") as file:
#     file.write(response.content)

#test post request
params = {
    'title'  : 'foo',
    'body'   : 'bar',
    'userId' : 1
}
response = requests.post('https://jsonplaceholder.typicode.com/posts', data=params)
print(response.status_code)
print(f"answer: {response.json()}")
