#!/usr/bin/env python3

# URL: http://www.pythonchallenge.com/pc/return/balloons.html
import difflib

import requests
import gzip


def main():
    username = 'huge'
    password = 'file'
    url = "http://www.pythonchallenge.com/pc/return/deltas.gz"
    local_file_name = url.split('/')[-1]
    response = requests.get(url, auth=(username, password))
    if response.status_code == 200:
        with open(local_file_name, 'wb') as f:
            f.write(response.content)

    data = gzip.open(local_file_name)
    d1, d2 = "", ""
    for line in data:
        d1 += (line[:53].decode() + "\n")
        d2 += (line[56:].decode())

    compare = difflib.Differ().compare(d1.split("\n"), d2.split("\n"))
    img1 = open("img1.png", "wb")
    img2 = open("img2.png", "wb")
    img3 = open("img3.png", "wb")

    for line in compare:
        bs = bytes.fromhex("".join(line[2:].strip().split(" ")))
        if line[0] == '+':
            img1.write(bs)
        elif line[0] == '-':
            img2.write(bs)
        else:
            img3.write(bs)

    img1.close()
    img2.close()
    img3.close()


if __name__ == "__main__":
    main()
