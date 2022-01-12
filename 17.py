#!/usr/bin/env python3

# URL: http://www.pythonchallenge.com/pc/return/romance.html
from urllib.request import Request, urlopen

import requests
import re
from urllib.parse import unquote, quote_plus
import bz2
import xmlrpc.client

from future.backports.urllib.parse import unquote_to_bytes


def main():
    url = "http://www.pythonchallenge.com/pc/def/linkedlist.php"
    response = requests.get(url)
    print(unquote(response.cookies['info']))

    busy_nothing = '12345'
    pattern = r'and the next busynothing is (\d*)'

    cookies_data = []
    for i in range(1, 400):
        response = requests.get(url, params={"busynothing": busy_nothing})
        assert response.status_code == 200
        cookies_data.append(response.cookies['info'])
        regex_res = re.search(pattern, response.text)
        if regex_res:
            busy_nothing = regex_res.group(1)
        else:
            cookies_data = "".join(cookies_data)
            break

    cookies_data = unquote_to_bytes(cookies_data.replace("+", " "))
    print(bz2.decompress(cookies_data).decode())

    conn = xmlrpc.client.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
    print(conn.phone("Leopold"))

    url = "http://www.pythonchallenge.com/pc/stuff/violin.php"
    msg = "the flowers are on their way"

    req = requests.get(url, cookies={'info': msg})
    print(req.text)


if __name__ == "__main__":
    main()
