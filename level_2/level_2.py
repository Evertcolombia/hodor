#!/usr/bin/python3

import requests

try:
    session = requests.Session()
    url = 'http://158.69.76.135/level2.php'
head = {}
get = session.get(url)
cookie = dict(session.cookies)

my_obj = {"id": '1255', 'holdthedoor': 'Submit', 'key': cookie['HoldTheDoor']}
head.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'})
head.update({'Referer': url})

response = session.post(url, my_obj, headers=head)
print("done")
