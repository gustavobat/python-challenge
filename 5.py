#!/usr/bin/env python3

# URL: http://www.pythonchallenge.com/pc/def/peak.html
import pickle


def main():
    with open('5.in', 'rb') as f:
        data = pickle.load(f)
    for line in data:
        print("".join([char * occurrences for char, occurrences in line]))


if __name__ == "__main__":
    main()
