#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/8/26 14:48
# @Author : way
# @Site :
# @Describe:

from flask import Flask, render_template
from data import *

app = Flask(__name__)


@app.route('/')
def index():
    data = IndexData()
    # stu_list = data.a.keys
    return render_template('indexNew.html', form=data)

@app.route('/per/<uid>')
def per(uid):
    data = StuData(uid)
    data.uid = uid
    # stu_list = data.a.keys
    return render_template('indexstu.html', form=data)

if __name__ == "__main__":
    app.run(host='127.0.0.1',port=8081, debug=True)
