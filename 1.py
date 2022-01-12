#!/usr/bin/env python3

# URL: http://www.pythonchallenge.com/pc/def/map.html

import string


def shift_text(text, shift):
    letters = string.ascii_lowercase
    shifted_letters = letters[shift:] + letters[:shift]

    return text.translate(letters.maketrans(letters, shifted_letters))


def main():
    riddle = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq " \
             "ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq" \
             " rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
    shift = 2

    riddle_translate = shift_text(riddle, shift)
    print(riddle_translate)

    solution = shift_text("map", shift)
    print(solution)


if __name__ == "__main__":
    main()
