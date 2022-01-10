#!/usr/bin/env python3

# URL: http://www.pythonchallenge.com/pc/return/bull.html

import re


def look_n_say(current):
    regex_match = re.findall(r"([0-9])(\1*)", current)
    next_num = "".join(str(len(match[0]) + len(match[1])) + match[0] for match in regex_match)
    return next_num


def main():
    sequence = ['1']
    for i in range(0, 30):
        sequence.append(look_n_say(sequence[-1]))

    print(len(sequence[30]))


if __name__ == "__main__":
    main()
