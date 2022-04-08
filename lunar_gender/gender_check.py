#!/usr/bin/python
# _*_ coding: UTF-8 _*_
import sys
from datetime import datetime

from predict.gender_predict import GenderPredict


class GenderCheck:
    def __init__(self, argv, script=False):
        self.status = -1
        self.age = ''
        self.gender = ''
        self.date = ''
        self.birthday = None
        self.date_genders = []
        date_str = ''
        if script:
            if not isinstance(argv, list) or len(argv) == 0:
                print('input is not right')
                return
                pass
            date_str = argv[0]
            pass
        else:
            if not isinstance(argv, str):
                print('input is not right')
                return
                pass
            date_str = argv
            pass
        dates = date_str.split('.')
        if len(dates) != 3:
            print('input is not right')
            return
            pass
        western_birthday = None
        try:
            western_birthday = datetime(int(dates[0]), int(dates[1]), int(dates[2]))
        except Exception as e:
            print('input is not right')
            return
        pass

        if western_birthday is None:
            print('input is not right')
            return
            pass
        today = datetime.today()
        if western_birthday > today:
            print("the input date is later than today")
            return
            pass
        self.birthday = western_birthday
        pass

    def check_pregrancy_gender(self, type=0):
        if self.birthday is None:
            return
            pass
        if type == 0:
            self.check_gender()
            pass
        elif type == 1:
            self.check_genders()
        pass

    def check_gender(self):
        gender_predict = GenderPredict(self.birthday)
        age, date, gender = gender_predict.check()
        if len(gender):
            self.status = 0
            self.date = date.strftime('%B %Y')
            self.age = str(age)
            self.gender = gender
            print(self.age + ", " + self.date + ", " + self.gender)
            pass
        pass

    def check_genders(self):
        gender_predict = GenderPredict(self.birthday)
        date_genders = gender_predict.check_next_12_month()
        if len(date_genders):
            self.status = 0
            pass
        for dic in date_genders:
            date: datetime = dic['date']
            gender = dic['gender']
            age = dic['age']
            date_str = date.strftime('%B %Y')
            self.date_genders.append({'age': age, 'date': date_str, 'gender': gender})
            if len(gender):
                print(str(age) + ", " + date_str + ", " + gender)
                pass
            else:
                print(str(age) + ", " + date_str + ", we cannot predict")
                pass
            pass
        pass

    pass


def test2():
    date = datetime(1990, 1, 18)
    gender_predict = GenderPredict(date)
    date_genders = gender_predict.check_next_12_month()
    for dic in date_genders:
        date: datetime = dic['date']
        gender = dic['gender']
        age = dic['age']
        date_str = date.strftime('%B %Y')
        if len(gender):
            print(str(age) + ", " + date_str + ", " + gender)
            pass
        else:
            print(str(age) + ", " + date_str + ", we cannot predict")
            pass
        pass

    pass


def test():
    date = datetime(1990, 1, 18)
    gender_predict = GenderPredict(date)
    age, date, gender = gender_predict.check()
    if len(gender):
        date_str = date.strftime('%B %Y')
        print(str(age) + ", " + date_str + ", " + gender)
        pass
    pass


if __name__ == '__main__':
    # python3 gender_check.py 1915.2.28
    # test()
    check = GenderCheck(sys.argv[1:], True)
    # check = GenderCheck('1995.1.28')
    check.check_pregrancy_gender(0)
    exit(0)
