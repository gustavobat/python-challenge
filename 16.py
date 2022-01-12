#!/usr/bin/env python3

# URL: http://www.pythonchallenge.com/pc/return/mozart.html

from PIL import Image, ImageChops
import requests


def main():
    username = 'huge'
    password = 'file'
    url = 'http://www.pythonchallenge.com/pc/return/mozart.gif'
    local_file_name = url.split('/')[-1]
    response = requests.get(url, auth=(username, password))
    if response.status_code == 200:
        with open(local_file_name, 'wb') as f:
            f.write(response.content)

    with Image.open(local_file_name) as img:
        for y in range(img.height):
            box = (0, y, img.width, y + 1)
            row = img.crop(box)
            pink_pos = row.tobytes().index(195)
            row = ImageChops.offset(row, -pink_pos)
            img.paste(row, box)

        img.show()


if __name__ == "__main__":
    main()
