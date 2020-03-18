#!/usr/bin/python3

import requests, sys

try:
    session = requests.Session()
    url = 'http://158.69.76.135/level2.php'
    head = {}
    get = session.get(url)
    print("connectins a session from the url and gettng a response")
except:
    raise ValueError("error")
    sys.exit(1)

try:
    cookie = dict(session.cookies)
except:
    print("Error getting the cookies")
    sys.exit(1)

my_obj = {"id": '1255', 'holdthedoor': 'Submit', 'key': cookie['HoldTheDoor']}


""" USe the head dict yto set up an user agent and a  referer
    
        User Agent: the OS where the reques comes
        Refere: the lin where the request comes we use the same adress"""
try:
    head.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'})
    head.update({'Referer': url})
except:
    print("header Error")
    sys.exit(1)

#send the respons to the url passing the url obj, and header
response = session.post(url, my_obj, headers=head)
print("done")
