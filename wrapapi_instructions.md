pip3 install flask
pip3 install waitress

cd into the directory of lunar_gender, run:
python3 predict_api.py

then open such following url in safari, chrome or curl.
http://linhua.free.idcfengye.com/child_gender?birthday=1995.1.28&type=1
http://linhua.free.idcfengye.com/child_gender?birthday=1995.1.28&type=0
http://linhua.free.idcfengye.com/child_gender?birthday=1995.1.28
http://linhua.free.idcfengye.com/lunar_age?birthday=1995.1.28

Params:
1) type: type default is 0, it can be empty, 0 means next month, 1 means next 12 months
2) birthday : birthday is the mother birthday, it can not be empty