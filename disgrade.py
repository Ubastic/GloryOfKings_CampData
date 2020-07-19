
# -*- coding:utf-8  -*-
import requests
import json
import sys
import time

store = []

# params 接收一个字典或者字符串的查询参数，字典类型自动转换为url编码，不需要urlencode()
lasttime=0
json_ob = {}
with open("detailwin.json", "r") as f:
    for ov in f :
        ov = json.loads(ov.strip())
        json_ob = ov
def get_title(json_ob):
    dat = []
    for t in json_ob:
        for i in t:
            dat.append(i)
    return dat
dat = get_title(json_ob)
print(dat)

for index,t in enumerate(json_ob):
    if(t['battleType']=="30" or 'acntcampBlue' not in t.keys()):
        print("五军对决")
        continue
    sumBlue = 0
    sumRed = 0
    for j in t['acntcampBlue']:
        score = int(j['disGradeLevelId'])
        if(score==None):
            continue
        sumBlue+=score
    for j in t['acntcampRed']:
        score = int(j['disGradeLevelId'])
        if(score==None):
            continue
        sumRed+=score
    json_ob[index]['BlueGrade'] = sumBlue
    json_ob[index]['RedGrade'] = sumRed
    if(t['myPlayCamp']=="red"):
        json_ob[index]['gradeType'] = "上分局" if sumRed>sumBlue else "掉分局"
        if(t['win']=="win"):
            json_ob[index]['gradeTrue'] = "True" if sumRed>sumBlue else "False"
        else:
            json_ob[index]['gradeTrue'] = "True" if sumRed<sumBlue else "False"
    else:
        json_ob[index]['gradeType'] = "上分局" if sumBlue>sumRed else "掉分局"
        if(t['win']=="win"):
            json_ob[index]['gradeTrue'] = "True" if sumRed<sumBlue else "False"
        else:
            json_ob[index]['gradeTrue'] = "True" if sumRed<sumBlue else "False"
    print(sumBlue)
    print(sumRed)
    #print(json_ob[index]['eolType'])
    #time.sleep(1)


filename='detailgrade.json'
with open(filename,'w') as file_obj:
    json.dump(json_ob,file_obj)
