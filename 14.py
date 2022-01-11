#!/usr/bin/env python3

# URL: http://www.pythonchallenge.com/pc/return/italy.html
import operator

from PIL import Image
import requests


def get_strides(size):
    stride = [size]
    for i in range(size - 1, 0, -1):
        stride.append(i)
        stride.append(i)
    return stride


def main():
    username = 'huge'
    password = 'file'
    url = 'http://www.pythonchallenge.com/pc/return/wire.png'
    local_file_name = url.split('/')[-1]
    response = requests.get(url, auth=(username, password))
    if response.status_code == 200:
        with open(local_file_name, 'wb') as f:
            f.write(response.content)

    strides = get_strides(100)

    with Image.open(local_file_name) as img:
        hidden_img = Image.new("RGBA", (100, 100), (0, 0, 0, 255))
        current_pos = (0, 0)

        total_pix = 0
        for s_id in range(len(strides)):
            if s_id % 4 == 0:
                pos_increment = (1, 0)
            elif s_id % 4 == 1:
                pos_increment = (0, 1)
            elif s_id % 4 == 2:
                pos_increment = (-1, 0)
            elif s_id % 4 == 3:
                pos_increment = (0, -1)

            stride = strides[s_id]
            for i in range(stride):
                hidden_img.putpixel(current_pos, img.getpixel((total_pix, 0)))
                total_pix += 1
                if i != stride - 1:
                    current_pos = list(map(operator.add, current_pos, pos_increment))
        hidden_img.show()


if __name__ == "__main__":
    main()
