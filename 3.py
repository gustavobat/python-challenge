#!/usr/bin/env python3

# URL: http://www.pythonchallenge.com/pc/def/equality.html

def find_subsequence(query, base):
    positions = list()
    for i in range(len(base)):
        if base[i:i + len(query)] == query:
            positions.append(i)
    return positions


def main():
    target = [False, True, True, True, False, True, True, True, False]

    text_file = open("3.in", "r")
    riddle = text_file.read().replace("\n", "")
    text_file.close()

    is_upper_case = map(lambda x: True if x.isupper() else False, riddle)

    positions = find_subsequence(target, is_upper_case)
    solution = ""
    for pos in positions:
        solution += riddle[pos:pos + len(target)][4]
    print(solution)


if __name__ == "__main__":
    main()
