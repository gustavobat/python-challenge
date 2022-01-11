#!/usr/bin/env python3

# URL: http://www.pythonchallenge.com/pc/return/5808.html

from PIL import Image
import requests


def main():
    username = 'huge'
    password = 'file'
    url = 'http://www.pythonchallenge.com/pc/return/cave.jpg'
    local_file_name = url.split('/')[-1]
    response = requests.get(url, auth=(username, password))
    if response.status_code == 200:
        with open(local_file_name, 'wb') as f:
            f.write(response.content)

    with Image.open(local_file_name) as img:
        hidden_img1 = Image.new("RGBA", (img.width // 2, img.height // 2), (0, 0, 0, 255))
        hidden_img2 = Image.new("RGBA", (img.width // 2, img.height // 2), (0, 0, 0, 255))
        for i in range(img.width):
            for j in range(img.height):
                if (i + j) % 2 == 0:
                    hidden_img1.putpixel((i // 2, j // 2), img.getpixel((i, j)))
                else:
                    hidden_img2.putpixel((i // 2, j // 2), img.getpixel((i, j)))

        hidden_img1.show("hidden_img1")
        hidden_img2.show("hidden_img2")


if __name__ == "__main__":
    main()
