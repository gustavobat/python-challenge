#!/usr/bin/env python3

# URL: http://www.pythonchallenge.com/pc/def/ocr.html

from collections import Counter
import urllib.request
import re


def main():
    html = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/ocr.html").read().decode()
    riddle = re.findall("<!--(.*?)-->", html, re.DOTALL)[-1]

    counter = Counter(riddle)

    for i in counter.items():
        if i[1] > 100:
            riddle = riddle.replace(str(i[0]), "")

    print(riddle)


if __name__ == "__main__":
    main()
