#!/usr/bin/env python3

# URL: http://www.pythonchallenge.com/pc/def/ocr.html

from collections import Counter


def main():
    text_file = open("2.in", "r")
    riddle = text_file.read()
    text_file.close()

    counter = Counter(riddle)

    for i in counter.items():
        if i[1] > 100:
            riddle = riddle.replace(str(i[0]), "")

    print(riddle)


if __name__ == "__main__":
    main()
