#!/usr/bin/python
# _*_ coding: UTF-8 _*_
import sys
from datetime import datetime

from gender_predict import GenderPredict


class GenderCheck:
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
        self.check_gender(western_birthday)
        pass

    pass

    def check_gender(self, date: datetime):
        gender_predict = GenderPredict(date)
        gender_predict.check()
        if len(gender_predict.gender):
            print(gender_predict.predict_month + ":  " + gender_predict.gender)
            pass
        pass

    pass


def test():
    date = datetime(1996, 1, 18)
    gender_predict = GenderPredict(date)
    gender_predict.check()
    if len(gender_predict.gender):
        print(gender_predict.predict_month + ":  " + gender_predict.gender)
        pass
    pass


if __name__ == '__main__':
    # python3 gender_check.py 1915.2.28
    # test()
    GenderCheck(sys.argv[1:])

    exit(0)
