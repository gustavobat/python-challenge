#!/usr/bin/env python3

# URL: http://www.pythonchallenge.com/pc/def/channel.html

import urllib
import zipfile
import re


def main():
    resource_url = "http://www.pythonchallenge.com/pc/def/channel.zip"
    local_file_name = resource_url.split('/')[-1]
    urllib.urlretrieve(resource_url, local_file_name)

    zip_data = zipfile.ZipFile(local_file_name)
    files = {name[:-4]: (
        zip_data.read(name).decode('utf-8'),
        zip_data.getinfo(name).comment.decode('utf-8')
    ) for name in zip_data.namelist()}

    nothing = '90052'
    comments = []
    pattern = r'Next nothing is (\d*)'

    while True:
        comments.append(files[nothing][1])
        text = files[nothing][0]
        regex_res = re.search(pattern, text)
        if regex_res:
            nothing = regex_res.group(1)
        else:
            break

    comments = "".join(comments)
    print(comments)


if __name__ == "__main__":
    main()
