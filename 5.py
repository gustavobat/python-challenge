#!/usr/bin/env python3

# URL: http://www.pythonchallenge.com/pc/def/peak.html

import pickle
from urllib.request import urlopen


def main():

    html = urlopen("http://www.pythonchallenge.com/pc/def/banner.p")
    data = pickle.load(html)
    for line in data:
        print("".join([char * occurrences for char, occurrences in line]))


if __name__ == "__main__":
    main()
