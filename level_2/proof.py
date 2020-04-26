#!/usr/bin/python3

import requests, os, bs4
import pytesseract
try:
    import Image
except ImportError:
    from PIL import Image

def image_request(image_url, count):

    res_img = requests.get(image_url)
    res.raise_for_status()

    img_path = os.path.join('capchat_images', ('img' + str(count) + '.png'))
    with open(img_path, 'wb') as img_file:
        for chunk in res_img.iter_content(100000):
            img_file.write(chunk)
    return img_path


def solve_image(img_path):
    img = Image.open(r"{}".format(img_path))
    save_path = img_path.split('.')[0]
    img = img.save(save_path, 'PNG')
    os.system("mv {} {}".format(save_path, img_path))

    string = pytesseract.image_to_string(Image.open(img_path))

    print(string)


count = 0
host = 'http://158.69.76.135'
os.makedirs('capchat_images', exist_ok=True)

res = requests.get(host + '/level3.php')
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')
image_src =  soup.form.find_all_next('img')[0].get('src')
image_url = host + image_src


################################################
img_path = image_request(image_url, count)
solve_image(img_path)
count += 1

