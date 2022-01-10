#!/usr/bin/env python3

# URL: http://www.pythonchallenge.com/pc/def/linkedlist.php

import requests
import re


def main():

    nothing = '12345'
    base_url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
    pattern = r'and the next nothing is (\d*)'

    for i in range(1, 400):
        response = requests.get(base_url + nothing)
        assert response.status_code == 200
        if response.text == "Yes. Divide by two and keep going.":
            nothing = str(int(nothing)/2)
            continue
        regex_res = re.search(pattern, response.text)
        if regex_res:
            nothing = regex_res.group(1)
        else:
            print(response.text)
            break


if __name__ == "__main__":
    main()
