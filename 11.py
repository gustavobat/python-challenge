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
        for row in range(img.width):
            for column in range(img.height):
                if (row + column) % 2 == 0:
                    hidden_img1.putpixel((row // 2, column // 2), img.getpixel((row, column)))
                else:
                    hidden_img2.putpixel((row // 2, column // 2), img.getpixel((row, column)))

        hidden_img1.show("hidden_img1")
        hidden_img2.show("hidden_img2")


if __name__ == "__main__":
    main()
