#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/8/26 14:48
# @Author : way
# @Site :
# @Describe:

from flask import Flask, render_template, jsonify
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



@app.route("/<data>/<uid>", methods=["GET"])
def stu(data, uid):
    data_scource = StuData(uid)
    if data == "audio":
        return jsonify({
            "stu": data_scource.stu_audio_hour_mean,
            "total": data_scource.total_audio_hour_mean
        })
    elif data == "phonelock":
        return jsonify({
            "stu": data_scource.stu_phonelock_day_count,
            "total": data_scource.total_phonelock_day_mean
        })

    elif data == "activity":
        return jsonify({
            "stu": data_scource.stu_activity_hour_mean,
            "total": data_scource.total_activity_hour_mean
        })


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)
