import json
from urllib.request import urlopen

with urlopen("https://jsonplaceholder.typicode.com/posts") as response:
    source = response.read()

data = json.loads(source)

# print(json.dumps(data, indent=2))

usd_rates = dict()
print("ids | title")
for item in data:
    print(item['id'] ,end=" ")
    print(item['title'])
    