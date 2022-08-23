import requests
url = 'http://172.18.58.80/index.php'
r = requests.get(url)
print(r.text)
