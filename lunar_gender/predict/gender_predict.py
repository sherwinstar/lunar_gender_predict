#!/usr/bin/python
# _*_ coding: UTF-8 _*_
import os
from datetime import datetime
from predict.lunar_age import LunarAge


class GenderPredict:
    def __init__(self, birth: datetime):
        self.unable_predict = []
        self.gender_predict = []
        self.birthday = birth
        self.lunar_age = LunarAge()
        self.load_gender_predict()
        self.load_unable_predict()
        self.status = 0
        self.message = ''
        pass

    def load_gender_predict(self):
        cur_path = os.path.abspath(os.path.dirname(__file__))
        child_gender_file = os.path.dirname(cur_path) + "/config/age_child_gender"
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
        child_gender_file = os.path.dirname(cur_path) + "/config/unable_predict"
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

    def check_next_12_month(self):
        date_genders = []
        if self.birthday is None:
            print("input date is not right")
            return date_genders
        date = datetime.today()
        month = date.month + 1
        year = date.year
        if month > 12:
            month = 1
            year = year + 1
            pass

        while len(date_genders) < 12:
            date = datetime(year, month, 1)
            age, gender = self.check_month(date)
            if len(gender):
                dic = {'age': age, 'date': date, 'gender': gender}
                date_genders.append(dic)
                pass
            else:
                dic = {'age': age, 'date': date, 'gender': ''}
                date_genders.append(dic)
            month = month + 1
            if month > 12:
                month = 1
                year = year + 1
                pass
            pass
        return date_genders
        pass

    def check_month(self, date: datetime):
        age = self.lunar_age.age_after_date(self.birthday, date)
        if self.birthday is None:
            print("input date is not right")
            return age, ''
        # date = datetime(2022, 1, 5)
        date = datetime.today()
        month = date.month
        year = date.year
        for dic in self.unable_predict:
            if int(dic['year']) == year and month == int(dic['month']):
                return age, ''
                pass
            pass

        # predict_month = date.strftime('%B')
        gender = ''

        # print(self.age)
        predict = False
        for dic in self.gender_predict:
            if int(dic["age"]) == age:
                genders = dic["genders"]
                if month <= len(genders):
                    sex = genders[month - 1]
                    predict = True
                    if sex == 'B':
                        gender = 'Boy'
                        break
                        pass
                    else:
                        gender = 'Girl'
                        break
                        pass
                    pass
                pass
            pass
        if predict == False:
            print("the lunar age is beyond predict")
            pass
        return age, gender
        pass

    def check(self):
        if self.birthday is None:
            print("input date is not right")
            return '', '', ''
        # date = datetime(2022, 1, 5)
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
                    pass
                predict_date = datetime(year, month, 1)
                self.status = 1
                self.message = "we cannot predict " + predict_date_next.strftime(
                    '%B %Y') + ", " + "but we will predict " + predict_date.strftime('%B %Y')
                print(self.message)
                break
                pass
            pass
        predict_date = datetime(year, month, 1)
        # predict_month = predict_date.strftime('%B')
        gender = ''
        age = self.lunar_age.age_after_date(self.birthday, predict_date)
        # print(self.age)
        predict = False
        for dic in self.gender_predict:
            if int(dic["age"]) == age:
                genders = dic["genders"]
                if month <= len(genders):
                    sex = genders[month - 1]
                    predict = True
                    if sex == 'B':
                        gender = 'Boy'
                        break
                        pass
                    else:
                        gender = 'Girl'
                        break
                        pass
                    pass
                pass
            pass
        if predict == False:
            print("the lunar age is beyond predict")
            pass
        return age, predict_date, gender
        pass


    pass
