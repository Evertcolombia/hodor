#!/usr/bin/python3

import requests, bs4, urllib


url = 'http://158.69.76.135/level3.php'
session = requests.session()
session = session.get(url)
cookie = dict(session.cookies)

soup = bs4.BeautifulSoup(session.text, 'html.parser')
img = soup.select('form > img')
print(img.src)
print(type(img))

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36',
    'Referer': url}

data = {'id': 1912, }

"""def do_connection():

    try:
        response = session.get('')
        print("connectins a session from the url and gettng a response")
    except:
        raise ValueError("An Error occurss when trying to get a session")
        sys.exit(1)

    try:
        cookie = dict(session.cookies)
        print("getting cookies")
        return cookie
    except:
        print("Error getting the cookies")
        sys.exit(1)

   
def header():
    USe the head dict yto set up an user agent and a  referer
    
        User Agent: the OS where the reques comes
        Refere: the lin where the request comes we
        use the same url

    try:
        head = {}
        head.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'})
        head.update({'Referer': url})
        print("send the response to the user Agent")
        return head
    except:
        print("header Error")
        sys.exit(1)


if len(argv) == 3:
    
    id = argv[1]
    url = argv[2]

    id = validate(id)
    session = requests.Session()

    for num  in range (1024):
    
        cookie = do_connection()

        my_obj = {"id": '125', 'holdthedoor': 'Submit', 'key': cookie['HoldTheDoor']}
        head = header()
        response = session.post(url, my_obj, headers=head)
        print("Success: {}".format(num))

print("Well Done. See you later hacker 8)")
"""
