
# -*- coding:utf-8  -*-
import requests
import json
import sys
headers = {
"Content-Encrypt":"",
"Accept-Encrypt":"",
"NOENCRYPT": "1",
"X-Client-Proto": "https",
"cChannelId": "",
"cClientVersionCode": "2020453409",
"cClientVersionName": "4.53.409",
"cCurrentGameId": "20001",
"cDeviceBrand": "Xiaomi",
"cDeviceCPU": "armeabi-v7a%24armeabi",
"cDeviceId": "b62fae5abb9422c34ce89a852c9833ef5927197f",
"cDeviceImei": "860758046354116",
"cDeviceMac": "02%3A00%3A00%3A00%3A00%3A00",
"cDeviceMem": "113917",
"cDeviceModel": "MI+8",
"cDeviceNet": "WIFI",
"cDevicePPI": "440",
"cDeviceSP": "%E4%B8%AD%E5%9B%BD%E7%A7%BB%E5%8A%A8",
"cDeviceScreenHeight": "2028",
"cDeviceScreenWidth": "1080",
"cGameId": "20001",
"cGzip": "1",
"cRand": "1595072761175",
"cSystem": "android",
"cSystemVersionCode": "28",
"cSystemVersionName": "9",
"deviceid": "b62fae5abb9422c34ce89a852c9833ef5927197f",
"gameAreaId": "3",
"gameId": "20001",
"gameOpenId": "owanlsjhh7xRwCKkzW6G_F7fqKIs",
"gameRoleId": "2386193908",
"gameServerId": "3232",
"gameUserSex": "1",
"tinkerId": "2020453409_0",
"token": "fEgtmsrN",
"userId": "1886577950",
"Host": "ssl.kohsocialapp.qq.com",
"X-Online-Host": "ssl.kohsocialapp.qq.com",
"x-tx-host": "ssl.kohsocialapp.qq.com",
"Content-Type": "application/x-www-form-urlencoded",
"Content-Length": "803",
"Connection": "Keep-Alive",
"Accept-Encoding": "gzip",
"User-Agent": "okhttp/3.12.0"}
params = {"apiVersion":"4",
"lastTime":"0",
"option":"0",
"roleId":"2386193908",
"cChannelId":"",
"cClientVersionCode":"2020453409",
"cClientVersionName":"4.53.409",
"cCurrentGameId":"20001",
"cDeviceBrand":"Xiaomi",
"cDeviceCPU":"armeabi-v7a$armeabi",
"cDeviceId":"b62fae5abb9422c34ce89a852c9833ef5927197f",
"cDeviceImei":"860758046354116",
"cDeviceMac":"02:00:00:00:00:00",
"cDeviceMem":"113917",
"cDeviceModel":"MI 8",
"cDeviceNet":"WIFI",
"cDevicePPI":"440",
"cDeviceSP":"中国移动",
"cDeviceScreenHeight":"2028",
"cDeviceScreenWidth":"1080",
"cGameId":"20001",
"cGzip":"1",
"cRand":"1595072761175",
"cSystem":"android",
"cSystemVersionCode":"28",
"cSystemVersionName":"9",
"deviceid":"b62fae5abb9422c34ce89a852c9833ef5927197f",
"gameAreaId":"3",
"gameId":"20001",
"gameOpenId":"owanlsjhh7xRwCKkzW6G_F7fqKIs",
"gameRoleId":"2386193908",
"gameServerId":"3232",
"gameUserSex":"1",
"tinkerId":"2020453409_0",
"token":"fEgtmsrN",
"userId":"1886577950"}
proxies = {
  "https": "http://localhost:8888",
}
store = []

# params 接收一个字典或者字符串的查询参数，字典类型自动转换为url编码，不需要urlencode()
lasttime=0
while(True):
    params['lastTime'] = lasttime
    response = requests.post("https://61.241.51.196:10001/play/getmatchlist", params, headers = headers,verify=False,proxies=proxies)
    js = response.json()
    lasttime = js['data']['lastTime']
    store.append(js['data']['list'])
    print(lasttime)
    if(js['data']['hasMore']==False):
        break
print(store)
filename='historyall.json'
with open(filename,'w') as file_obj:
    json.dump(store,file_obj)
# 查看响应内容，response.text 返回的是Unicode格式的数据
#print(response.text.encode('utf-8'))

# 查看响应内容，response.content返回的字节流数据
#print(response.content)

# 查看完整url地址
#print(response.url)

# 查看响应头部字符编码
#print(response.encoding)

# 查看响应码
#print(response.status_code)
