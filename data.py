#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/8/26 14:48
# @Author : way
# @Site : 
# @Describe:

import ujson as json


class IndexData():

    def __init__(self):

        with open('stu_alert_inf.json', 'r', encoding='utf-8') as f:
            data = json.loads(f.read())
            for i in data.keys():
                data[i]["失眠"] = data[i].pop("PSQI_True")
                data[i]["孤独"] = data[i].pop("lone_True")
                data[i]["抑郁"] = data[i].pop("PHQ_9_True")
                data[i]["压力"] = data[i].pop("stress_True")
            for i in data.keys():
                data[i] = dict(sorted(data[i].items(), key = lambda kv:(-kv[1], kv[0])))

            alert = {}
            for k,v in data.items():
                if v[list(v.keys())[0]] > 0.5:
                    alert[k] = list(v.keys())[0]
                else:
                    alert[k] = "健康"
            self.stu_list_alert = alert
            self.stu_list = data

        with open('./feature/activity/hour_mean.json', 'r', encoding='utf-8') as f:
            activity_hour_mean = json.loads(f.read())
            self.total_activity_hour_mean = activity_hour_mean

        with open('./feature/audio/hour_mean.json', 'r', encoding='utf-8') as f:
            audio_hour_mean = json.loads(f.read())
            self.total_audio_hour_mean = audio_hour_mean

        with open('./feature/phonelock/day_mean.json', 'r', encoding='utf-8') as f:
            phonelock_day_mean = json.loads(f.read())
            self.total_phonelock_day_mean = phonelock_day_mean


class StuData(IndexData):

    def __init__(self,uid):
        """
        按照 IndexData 的格式覆盖数据即可
        """
        super().__init__()
        with open(f'./feature/activity/per/{uid}_hour.json', 'r', encoding='utf-8') as f2:
            stu_activity_hour_mean = json.loads(f2.read())
            self.stu_activity_hour_mean = stu_activity_hour_mean

        with open(f'./feature/audio/per/{uid}_hour.json', 'r', encoding='utf-8') as f3:
            t = f3.read()
            stu_audio_hour_mean = json.loads(t)
            self.stu_audio_hour_mean = stu_audio_hour_mean

        with open(f'./feature/phonelock/per/{uid}.json', 'r', encoding='utf-8') as f4:
            phonelock_day_count = json.loads(f4.read())
            self.stu_phonelock_day_count = phonelock_day_count