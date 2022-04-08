#!/usr/bin/python
# _*_ coding: UTF-8 _*_


from flask import Flask, request
from gender_check import GenderCheck

app = Flask(__name__)
# app.debug = True


@app.route('/child_gender', methods=['GET'])
def child_gender():
    type = request.args.get('type', '0')
    birthday = request.args.get('birthday', '')
    check = GenderCheck(birthday)
    if type == '0':
        check.check_pregrancy_gender(0)
        if check.status == 0:
            data = {'age': check.age, 'date': check.date, 'gender': check.gender}
            return {
                "msg": "success",
                "status": 0,
                "data": data
            }
        elif check.status == 1:
            data = {'age': check.age, 'date': check.date, 'gender': check.gender}
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


@app.route('/', methods=['GET'])
def index():
    return 'Predict the child gender based on lunar age of mother\'s birthday.'
    pass


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
