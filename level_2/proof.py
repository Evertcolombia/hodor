#!/usr/bin/python3

import requests, os, bs4

host = 'http://158.69.76.135'
os.makedirs('capchat_images', exist_ok=True)

res = requests.get(host + '/level3.php')
res.raise_for_status()
count = 0

soup = bs4.BeautifulSoup(res.text, 'html.parser')
image_src =  soup.form.find_all_next('img')[0].get('src')
image_url = host + image_src

res_img = requests.get(image_url)
res.raise_for_status()

img_file = open(os.path.join('capchat_images', ('img' + str(count) + '.png')), 'wb')

count +=1
for chunk in res_img.iter_content(100000):
    img_file.write(chunk)
img_file.close()

