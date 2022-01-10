#!/usr/bin/env python3

# URL: http://www.pythonchallenge.com/pc/def/oxygen.html

from PIL import Image
import urllib.request
import re


def main():
    resource_url = "http://www.pythonchallenge.com/pc/def/oxygen.png"
    local_file_name = resource_url.split('/')[-1]
    urllib.request.urlretrieve(resource_url, local_file_name)

    with Image.open(local_file_name) as img:
        row = [img.getpixel((x, int(img.height / 2))) for x in range(img.width)]
        row = row[::7]
        hidden_message = map(chr, [r for r, g, b, a in row if r == g == b])

    hidden_message = "".join(hidden_message)
    print(hidden_message)

    regex_res = re.findall(r"(\d+)", hidden_message)
    solution = []
    for i in regex_res:
        solution.append(chr(int(i)))
    solution = "".join(solution)
    print(solution)


if __name__ == "__main__":
    main()
