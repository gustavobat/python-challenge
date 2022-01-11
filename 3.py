#!/usr/bin/env python3

# URL: http://www.pythonchallenge.com/pc/def/equality.html

import urllib.request
import re


def main():
    html = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/equality.html").read().decode()
    riddle = re.findall("<!--(.*)-->", html, re.DOTALL)[-1]
    print("".join(re.findall(r"[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]", riddle)))


if __name__ == "__main__":
    main()
