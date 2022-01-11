#!/usr/bin/env python3

# URL: http://www.pythonchallenge.com/pc/return/disproportional.html

import xmlrpc.client


def main():
    conn = xmlrpc.client.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
    print(conn.phone("Bert"))


if __name__ == "__main__":
    main()
