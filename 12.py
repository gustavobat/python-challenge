#!/usr/bin/env python3

# URL: http://www.pythonchallenge.com/pc/return/evil.html

import requests


def main():
    username = 'huge'
    password = 'file'
    url = 'http://www.pythonchallenge.com/pc/return/evil2.gfx'
    local_file_name = 'evil.gfx'
    response = requests.get(url, auth=(username, password))
    if response.status_code == 200:
        with open(local_file_name, 'wb') as f:
            f.write(response.content)

    data = open(local_file_name, 'rb').read()

    for i in range(5):
        open(str(12) + '-' + str(i) + '.jpg', 'wb').write(data[i::5])


if __name__ == "__main__":
    main()
