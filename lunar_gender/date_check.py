#!/usr/bin/python
# _*_ coding: UTF-8 _*_
import getopt
import sys
from datetime import datetime

from lunar_age import LunarAge


class DateCheck:
    def __init__(self, argv):
        if len(argv) == 0 or not isinstance(argv, list):
            print('input is not right')
            sys.exit(2)
            pass
        date_str = argv[0]
        dates = date_str.split('.')
        if len(dates) != 3:
            print('input is not right')
            sys.exit(2)
            pass
        western_birthday = None
        try:
            western_birthday = datetime(int(dates[0]), int(dates[1]), int(dates[2]))
        except Exception as e:
            print('input is not right')
            sys.exit(2)
        pass

        if western_birthday is None:
            print('input is not right')
            sys.exit(2)
            pass
        today = datetime.today()
        if western_birthday > today:
            print("the input date is later than today")
            exit(0)
            pass
        self.lunar_age(western_birthday)
        pass

    pass

    def lunar_age(self, date: datetime):
        lunar_age = LunarAge().age(date)
        print(lunar_age)
        pass


if __name__ == '__main__':
    # python3 date_check.py 1915.2.28
    DateCheck(sys.argv[1:])
    exit(0)
