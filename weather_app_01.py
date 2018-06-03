# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 17:00:55 2018

@author: lenovo
"""

import urllib.request as r
city_pinyin=input("请输入城市拼音:")
address='http://api.openweathermap.org/data/2.5/weather?q={}&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996'
info=r.urlopen(address.format(city_pinyin)).read().decode('utf-8','ignore')
print(info)

import json
data=json.loads(info)

print("欢迎使用全球天气app")
print("1.查看当前城市天气 2.查看其他城市天气 3.保存")
menu=input("请输入菜单：")
if menu=="1":
    print("1.查看当前城市天气")
    print("当前城市为:"+city_pinyin)
    print("天气为:"+str(data["weather"][0]['description']))
    print("压强为:"+str(data["main"]["pressure"]))
    print("最高温度为:"+str(data["main"]["temp_min"]))
    print("最低温度为:"+str(data["main"]["temp_max"]))
if menu=="2":
    print("2.查看其他城市天气")
if menu=="3":
    print("3.保存")
    
