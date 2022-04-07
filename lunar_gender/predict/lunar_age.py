#!/usr/bin/python
# _*_ coding: UTF-8 _*_
from datetime import datetime

from predict.lunar_date import LunarDate


class LunarAge:
    def __init__(self):
        pass

    def age(self, date: datetime):
        western_birthday = date
        birthday = LunarDate.from_datetime(western_birthday)  # 从阳历日期转换成农历日期对象
        today = LunarDate.today()
        lunar_age = today.lunar_year - birthday.lunar_year + 1
        return lunar_age
        pass

    def age_after_date(self, date: datetime, compare_date: datetime):
        western_birthday = date
        if compare_date is None:
            compare_date = datetime.today()
            pass
        birthday = LunarDate.from_datetime(western_birthday)  # 从阳历日期转换成农历日期对象
        lunar_compare_date = LunarDate.from_datetime(compare_date)
        lunar_age = lunar_compare_date.lunar_year - birthday.lunar_year + 1
        return lunar_age
        pass

    pass
