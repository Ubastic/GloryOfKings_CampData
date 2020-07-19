
# -*- coding:utf-8  -*-
import requests
import json
import sys
import time
headers = {
"X-Client-Proto":"https",
"User-Agent":"Mozilla/5.0 (Linux; U; Android 9; zh-cn; MI 8 Build/PKQ1.180729.001) AppleWebKit/533.1 (KHTML, like Gecko) Mobile Safari/533.1",
"noencrypt":"1",
"Accept-Encrypt":"",
"Host":"ssl.kohsocialapp.qq.com:10001",
"Accept-Encoding":"gzip",
"Content-Length":"2077",
"Content-Type":"application/x-www-form-urlencoded",
"Connection":"keep-alive"
}
params = {"encode":  "2",
"appVersion":  "2020453409",
"role":    "清兵啊别打团",
"toOpenid":    "owanlsjhh7xRwCKkzW6G_F7fqKIs",
"serverName":  "微信222区",
"source":  "smoba_zhushou",
"msdkEncodeParam": "71A004CF295E93C3089A83F534E36B089597A1539823A28E8FC1C845E4883489E313B6B2B096E252F4452FDE6AC56456F04617C12C9D85256C8F549A148460E52A0FBADA475009B8C7701E481E09E058146D4272F91FB55227BCFA23710B3E99D71B16A58CACC96D825DFB7BC9B6D8FF9A3F5D4F77F4B8FC1392F2D60E74D091B82E61D7EF312D213FDE5F2CACB9C7018097FB08E5BDF4F80C58EF15794BD3BB5E998CAFCCF192875666E0C28BAB61536CC262DFC58DEB81372620B81F20C95C984389E3CFC2BAEF3930FFA9EB694323563E4FDC4F158464DB63F2562B24F3C228F11EF4D62283C6857936EF99D821F07119968E67B3F5A9FD2103286E4C7FA9BBC54759A218D8CD2B6F3AD24ECB7323932097075535BD61B8CB0C275F7413EC75A507B1586EBBB677CC6DB2AADF17B1FA01A62D8C9832A9C06DC6845BE40E64981DF8AAE27865C88B058BA94D7FE30943DD02B8F00CF584",
"serverId":    "3232",
"sig": "38ce1182a17ac38e49f50cc61acbc415",
"wi":  "1",
"areaName":    "安卓",
"nickname":    " 　ZWNR",
"qi":  "1",
"toServerId":  "3232",
"modulename":  "battledetail",
"gameSeq": "1594826740",
"uin": "oFhrwsxpwaJp2xvgraEIcSKZVC-A",
"roleLevel":   "30",
"acntCamp":    "2",
"gameSvrId":   "53306",
"sourcePath":  "/data/user/0/com.tencent.gamehelper.smoba/files/hippy/battledetail/60/index.android.jsbundle",
"algorithm":   "v2",
"timestamp":   "1595089612440",
"toAreaId":    "3",
"gameId":  "20001",
"toGameOpenId":    "owanlsjhh7xRwCKkzW6G_F7fqKIs",
"toAppRoleId": "2386193908",
"roleId":  "242079734",
"openid":  "oFhrwsxpwaJp2xvgraEIcSKZVC-A",
"relaySvrId":  "823722243",
"env": "https://ssl.kohsocialapp.qq.com:10001",
"appVersionName":  "4.53.409",
"pvpType": "5",
"userId":  "1886577950",
"version": "3.1.96a",
"gameOpenid":  "owanlsjhh7xRwCKkzW6G_F7fqKIs",
"isMainRole":  "1",
"Brand":   "Xiaomi MI 8$",
"appOpenid":   "oFhrwsxpwaJp2xvgraEIcSKZVC-A",
"areaId":  "3",
"zn":  "安卓微信222区",
"platid":  "1",
"roleJob": "永恒钻石II",
"appid":   "wxf4b1e8a3e9aaf978",
"roleName":    "清兵啊别打团",
"toGameRoleId":    "242079734",
"z":   "3232",
"battleType":  "5",
"__instanceName__":    "battledetail",
"__instanceId__":  "140",
"gameOpenId":  "owanlsjhh7xRwCKkzW6G_F7fqKIs",
"fromType":    "1",
"msdkToken":   "[AWBYTCj9]"}


proxies = {
  "https": "http://localhost:8888",
}
store = []

# params 接收一个字典或者字符串的查询参数，字典类型自动转换为url编码，不需要urlencode()
lasttime=0
json_ob = {}
with open("historyall.json", "r") as f:
    for ov in f :
        ov = json.loads(ov.strip())
        json_ob = ov
def get_rows(json_ob):
    dat = []
    for t in json_ob:
        for i in t:
            #print(len(i))
            dat.append(i)
    return dat
dat = get_rows(json_ob)
q=0
#params['timestamp'] = int(round(time.time() * 1000))
gg=0
for i in dat:
    if(i["pvpType"]==1):
        continue
    q=q+1
    # if(q%7==0):
    #     time.sleep(2)
    # if(q%100==0):
    #     params['timestamp'] = int(round(time.time() * 1000))
    #     time.sleep(7)
    time.sleep(1)
    response = requests.post("https://ssl.kohsocialapp.qq.com:10001/role/h5getplaydetail", params, headers = headers,verify=False,proxies=proxies)
    js = response.json()
    if(js['result']==0):
        params['gameSeq'] = i["gameSeq"]
        params['gameSvrId'] = i["gameSvrId"]
        params['relaySvrId'] = i["relaySvrId"]
        params['acntCamp'] =  i["AcntCamp"]
        store.append(js['data'])
        print(js['data']['eventtime'])
    elif(js['returnCode']==-30314 or js['returnCode']==-10461):
        gg=0
        #params['timestamp'] = int(round(time.time() * 1000))
        params['msdkEncodeParam'] = input("msdkEncodeParam")
        params['msdkToken'] = input("msdkToken")
        params['sig'] = input("sig")
        params['timestamp'] = input("timestamp")
    else:
        time.sleep(5)
filename='detailall.json'
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
