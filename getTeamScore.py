
# -*- coding:utf-8  -*-
import requests
import json
import sys
import time
headers = {
"Content-Encrypt": "",
"Accept-Encrypt":  "",
"NOENCRYPT":   "1",
"X-Client-Proto":  "https",
"cChannelId":  "",
"cClientVersionCode":  "2020453409",
"cClientVersionName":  "4.53.409",
"cCurrentGameId":  "20001",
"cDeviceBrand":    "Xiaomi",
"cDeviceCPU":  "armeabi-v7a%24armeabi",
"cDeviceId":   "b62fae5abb9422c34ce89a852c9833ef5927197f",
"cDeviceImei": "860758046354116",
"cDeviceMac":  "02%3A00%3A00%3A00%3A00%3A00",
"cDeviceMem":  "113917",
"cDeviceModel":    "MI+8",
"cDeviceNet":  "WIFI",
"cDevicePPI":  "440",
"cDeviceSP":   "%E4%B8%AD%E5%9B%BD%E7%A7%BB%E5%8A%A8",
"cDeviceScreenHeight": "2028",
"cDeviceScreenWidth":  "1080",
"cGameId": "20001",
"cGzip":   "1",
"cRand":   "1595145604796",
"cSystem": "android",
"cSystemVersionCode":  "28",
"cSystemVersionName":  "9",
"deviceid":    "b62fae5abb9422c34ce89a852c9833ef5927197f",
"gameAreaId":  "3",
"gameId":  "20001",
"gameOpenId":  "owanlsjhh7xRwCKkzW6G_F7fqKIs",
"gameRoleId":  "2386193908",
"gameServerId":    "3232",
"gameUserSex": "1",
"tinkerId":    "2020453409_0",
"token":   "fEgtmsrN",
"userId":  "1886577950",
"Host":    "ssl.kohsocialapp.qq.com",
"X-Online-Host":   "ssl.kohsocialapp.qq.com",
"x-tx-host":   "ssl.kohsocialapp.qq.com",
"Content-Type":    "application/x-www-form-urlencoded",
"Content-Length":  "793",
"Connection":  "Keep-Alive",
"Accept-Encoding": "gzip",
"User-Agent":  "okhttp/3.12.0"
}
params = {
"friendUserId":    "2140784032",
"roleId":  "981226610",
"cChannelId":  "",
"cClientVersionCode":  "2020453409",
"cClientVersionName":  "4.53.409",
"cCurrentGameId":  "20001",
"cDeviceBrand":    "Xiaomi",
"cDeviceCPU":  "armeabi-v7a$armeabi",
"cDeviceId":   "b62fae5abb9422c34ce89a852c9833ef5927197f",
"cDeviceImei": "860758046354116",
"cDeviceMac":  "02:00:00:00:00:00",
"cDeviceMem":  "113917",
"cDeviceModel":    "MI 8",
"cDeviceNet":  "WIFI",
"cDevicePPI":  "440",
"cDeviceSP":   "中国移动",
"cDeviceScreenHeight": "2028",
"cDeviceScreenWidth":  "1080",
"cGameId": "20001",
"cGzip":   "1",
"cRand":   "1595145604796",
"cSystem": "android",
"cSystemVersionCode":  "28",
"cSystemVersionName":  "9",
"deviceid":    "b62fae5abb9422c34ce89a852c9833ef5927197f",
"gameAreaId":  "3",
"gameId":  "20001",
"gameOpenId":  "owanlsjhh7xRwCKkzW6G_F7fqKIs",
"gameRoleId":  "2386193908",
"gameServerId":    "3232",
"gameUserSex": "1",
"tinkerId":    "2020453409_0",
"token":   "fEgtmsrN",
"userId":  "1886577950"}


proxies = {
  "https": "http://localhost:8888",
}
store = []

# params 接收一个字典或者字符串的查询参数，字典类型自动转换为url编码，不需要urlencode()
lasttime=0
json_ob = {}
with open("detailall.json", "r") as f:
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
def getUserScore(roleId,userId):
    params['friendUserId'] = userId
    params['roleId'] = roleId
    response = requests.post("https://61.241.51.196:10001/game/battleprofile", params, headers = headers,verify=False,proxies=proxies)
    js = response.json()
    if(js['data']['rolecard']!={}):
        return js['data']['rolecard']['totalGrade']
    else:
        return None
for index,t in enumerate(json_ob):
    if(t['battleType']=="30" or 'acntcampBlue' not in t.keys()):
        print("五军对决")
        continue
    sumBlue = 0
    sumRed = 0
    for j in t['acntcampBlue']:
        score = getUserScore(j['roleId'],j['userId'])
        if(score==None):
            continue
        sumBlue+=score
        print()
    for j in t['acntcampRed']:
        score = getUserScore(j['roleId'],j['userId'])
        if(score==None):
            continue
        sumRed+=score
    json_ob[index]['BlueScore'] = sumBlue
    json_ob[index]['RedScore'] = sumRed
    if(t['myPlayCamp']=="red"):
        json_ob[index]['eolType'] = "上分局" if sumRed>sumBlue else "掉分局"
    else:
        json_ob[index]['eolType'] = "上分局" if sumBlue>sumRed else "掉分局"
    print(sumBlue)
    print(sumRed)
    print(json_ob[index]['eolType'])
    #time.sleep(1)


filename='detailsum.json'
with open(filename,'w') as file_obj:
    json.dump(json_ob,file_obj)
