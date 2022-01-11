#!/usr/bin/env python3

# URL: http://www.pythonchallenge.com/pc/def/equality.html

import urllib.request
import re


def find_subsequence(query, base):
    positions = list()
    for i in range(len(base)):
        if base[i:i + len(query)] == query:
            positions.append(i)
    return positions


def main():
    target = [False, True, True, True, False, True, True, True, False]

    html = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/equality.html").read().decode()
    riddle = re.findall("<!--(.*)-->", html, re.DOTALL)[-1]

    is_upper_case = map(lambda x: True if x.isupper() else False, riddle)

    positions = find_subsequence(target, list(is_upper_case))
    solution = ""
    for pos in positions:
        solution += riddle[pos:pos + len(target)][4]
    print(solution)


if __name__ == "__main__":
    main()
