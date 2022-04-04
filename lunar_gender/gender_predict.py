#!/usr/bin/python
# _*_ coding: UTF-8 _*_
import os
from datetime import datetime
from lunar_age import LunarAge


class GenderPredict:
    def __init__(self, birth: datetime):
        self.unable_predict = []
        self.gender_predict = []
        self.birthday = birth
        self.gender = ''
        self.predict_month = ''
        self.lunar_age = LunarAge()
        self.load_gender_predict()
        self.load_unable_predict()
        pass

    def load_gender_predict(self):
        cur_path = os.path.abspath(os.path.dirname(__file__))
        child_gender_file = cur_path + "/config/age_child_gender"
        with open(child_gender_file, 'r') as f:
            data = f.read()
            mapping = data.split("\n")

            for item in mapping:
                dic = {}
                items = item.split(":")
                if len(items) == 2:
                    dic["age"] = items[0]
                    genders = items[1].split(",")
                    dic["genders"] = genders
                    self.gender_predict.append(dic)
                    pass
                pass
            pass
        pass

    def load_unable_predict(self):
        cur_path = os.path.abspath(os.path.dirname(__file__))
        child_gender_file = cur_path + "/config/unable_predict"
        with open(child_gender_file, 'r') as f:
            data = f.read()
            mapping = data.split("\n")
            for item in mapping:
                dic = {}
                items = item.split(" ")
                if len(items) == 2:
                    dic["year"] = items[0]
                    dic["month"] = items[1]
                    self.unable_predict.append(dic)
                    pass
                pass
            pass
        pass

    def check(self):
        if self.birthday is None:
            print("input date is not right")
            return
        # date = datetime(2022, 5, 5)
        date = datetime.today()
        month = date.month + 1
        year = date.year
        if month > 12:
            month = 1
            year = year + 1
            pass
        for dic in self.unable_predict:
            if int(dic['year']) == year and month == int(dic['month']):
                predict_date_next = datetime(year, month, 1)
                month = month + 1
                if month > 12:
                    month = 1
                    year = year + 1
                    predict_date = datetime(year, month, 1)
                    print("we cannot predict " + predict_date_next.strftime(
                        '%B') + ", " + "but we will predict " + predict_date.strftime('%B'))
                    pass
                else:
                    predict_date = datetime(year, month, 1)
                    print("we cannot predict " + predict_date_next.strftime(
                        '%B') + ", " + "but we will predict " + predict_date.strftime('%B'))
                    pass
                break
                pass
            pass
        predict_date = datetime(year, month, 1)
        self.predict_month = predict_date.strftime('%B')
        age = self.lunar_age.age(self.birthday)
        # print(age)
        predict = False
        for dic in self.gender_predict:
            if int(dic["age"]) == age:
                genders = dic["genders"]
                if month <= len(genders):
                    sex = genders[month - 1]
                    predict = True
                    if sex == 'B':
                        self.gender = 'boy'
                        break
                        pass
                    else:
                        self.gender = 'girl'
                        break
                        pass
                    pass
                pass
            pass
        if predict == False:
            print("the lunar age is beyond predict")
            pass
        pass

    pass
