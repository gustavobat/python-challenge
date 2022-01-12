#!/usr/bin/env python3

# URL: http://www.pythonchallenge.com/pc/return/uzi.html

import calendar
import datetime


def main():
    possible_dates = []
    for year in range(1006, 1997, 10):
        date_obj = datetime.date(year, 1, 27)
        if calendar.isleap(year) and date_obj.isoweekday() == 2:
            possible_dates.append(date_obj.isoformat())
    print(possible_dates[-2])  # Mozart's birthday


if __name__ == "__main__":
    main()
