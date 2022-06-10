#!/usr/bin/python
# _*_ coding: UTF-8 _*_


from flask import Flask, request
from waitress import serve
from predict.lunar_age import LunarAge
from gender_check import GenderCheck

app = Flask(__name__)


@app.route('/lunar_age', methods=['GET'])
def lunar_age():
    birthday = request.args.get('birthday', '')
    lunar = LunarAge()
    age = lunar.age_from_date(birthday)
    if age == -1:
        return {
            "msg": "error",
            "status": -1,
            "data": {}
        }
    else:
        data = {'age': age}
        return {
            "msg": "success",
            "status": 0,
            "data": data
        }
    pass


@app.route('/child_gender', methods=['GET'])
def child_gender():
    type = request.args.get('type', '0')
    birthday = request.args.get('birthday', '')
    check = GenderCheck(birthday)
    if type == '0':
        check.check_pregrancy_gender(0)
        if check.status == 0:
            data = {'age': check.age, 'date': check.date, 'gender': check.gender, 'month_slug': check.month_slug,
                    'year': check.year, 'gender_slug': check.gender_slug}
            return {
                "msg": "success",
                "status": 0,
                "data": data
            }
        elif check.status == 1:
            data = {'age': check.age, 'date': check.date, 'gender': check.gender, 'month_slug': check.month_slug,
                    'year': check.year, 'gender_slug': check.gender_slug}
            return {
                "msg": check.message,
                "status": 1,
                "data": data
            }
        else:
            data = {}
            return {
                "msg": "error",
                "status": -1,
                "data": data
            }
        pass
    elif type == '1':
        check.check_pregrancy_gender(1)
        if check.status == 0:
            data = check.date_genders
            return {
                "msg": "success",
                "status": 0,
                "data": data
            }
        else:
            data = []
            return {
                "msg": "error",
                "status": -1,
                "data": data
            }
        pass
    else:
        return {
            "msg": "error",
            "status": -1
        }
    pass


# http://127.0.0.1:8080/childGender?momBirthday=1995.1.28&dadBirthday=1995.1.28&kidAges=12,14,15&kidGenders=0,1,1
@app.route('/childGender', methods=['GET'])
def childGender():
    type = request.args.get('type', '0')
    birthday = request.args.get('momBirthday', '')
    dadBirthday = request.args.get('dadBirthday', '')
    kidAges = request.args.get('kidAges', '')
    kidGenders = request.args.get('kidGenders', '')
    check = GenderCheck(birthday)
    if type == '0':
        check.check_pregrancy_gender(0)
        if check.status == 0:
            data = {'age': check.age, 'date': check.date, 'gender': check.gender, 'month_slug': check.month_slug,
                    'year': check.year, 'gender_slug': check.gender_slug}
            return {
                "msg": "success",
                "status": 0,
                "data": {"data": data,
                         "momBirthday": birthday,
                         "dadBirthday": dadBirthday,
                         "kidAges": kidAges,
                         "kidGenders": kidGenders
                         }
            }
        elif check.status == 1:
            data = {'age': check.age, 'date': check.date, 'gender': check.gender, 'month_slug': check.month_slug,
                    'year': check.year, 'gender_slug': check.gender_slug}
            return {
                "msg": check.message,
                "status": 1,
                "data": {"data": data,
                         "momBirthday": birthday,
                         "dadBirthday": dadBirthday,
                         "kidAges": kidAges,
                         "kidGenders": kidGenders
                         }
            }
        else:
            data = {}
            return {
                "msg": "error",
                "status": -1,
                "data": data
            }
        pass
    elif type == '1':
        check.check_pregrancy_gender(1)
        if check.status == 0:
            data = check.date_genders
            return {
                "msg": "success",
                "status": 0,
                "data": {"data": data,
                         "momBirthday": birthday,
                         "dadBirthday": dadBirthday,
                         "kidAges": kidAges,
                         "kidGenders": kidGenders
                         }
            }
        else:
            data = {}
            return {
                "msg": "error",
                "status": -1,
                "data": data
            }
        pass
    else:
        return {
            "msg": "error",
            "status": -1,
            "data": {}
        }
    pass


@app.route('/', methods=['GET'])
def index():
    return '<b>Predict the child gender based on lunar age of mother\'s birthday.</b>' \
           '<p>http://127.0.0.1/child_gender?birthday=2001.10.5&type=1&type=1</p>' \
           '<p>http://127.0.0.1/child_gender?birthday=1995.1.28&type=0</p>' \
           '<p>http://127.0.0.1/child_gender?birthday=1995.1.28</p>' \
           '<p>http://127.0.0.1/childGender?momBirthday=1995.1.28&dadBirthday=1995.1.28&kidAges=12,14,15&kidGenders=0,1,1</p>' \
           '<p>http://127.0.0.1/childGender?momBirthday=1995.1.28&dadBirthday=1992.3.28&kidAges=12,14,15&kidGenders=0,1,1&type=1</p>' \
           '<p>type default is 0, 0 means next month, 1 means next 12 months</p>' \
           '<p>birthday is the mother birthday, it can not be empty</p>'
    pass


if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=8080)
    serve(app, host="0.0.0.0", port=80)
