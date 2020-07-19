
# -*- coding:utf-8  -*-
import requests
import json
import sys
headers = {
"X-Client-Proto":  "https",
"User-Agent":  "Mozilla/5.0 (Linux; U; Android 9; zh-cn; MI 8 Build/PKQ1.180729.001) AppleWebKit/533.1 (KHTML, like Gecko) Mobile Safari/533.1",
"noencrypt":   "1",
"Accept-Encrypt":  "",
"Content-Type":    "application/x-www-form-urlencoded; charset=UTF-8",
"Content-Length":  "2039",
"Host":    "ssl.kohsocialapp.qq.com:10001",
"Connection":  "Keep-Alive",
"Accept-Encoding": "gzip"}
params = {"encode":  "2",
"appVersion":  "2020453409",
"role":    "清兵啊别打团",
"toOpenid":    "owanlsjhh7xRwCKkzW6G_F7fqKIs",
"serverName":  "微信222区",
"source":  "smoba_zhushou",
"msdkEncodeParam": "66C57603D43368BA738454A96B342940ED02CAC8C62F66665EE5A0B934BA9E71226E79BE5F173A646DB11C286E2F9B002697EBBE093FCEBB722D1EE2A04963DC6B3CB46CA838EB97F8F2E2BF348A9D82D50FC3A0CA09C710389570F98220BFB2EF5D2FAD1622905EA3C2FA17AD6316F3E39FEDB5012A49DB3F5ED92934584BA19F0F7927C1EEE36E1C38E8B6135D2BCD1C474CBA6B656BC6AEB138CBB7127EAAE08BAFAC8A289308F3742B167B6AF8EAB47874C90940E9F0382ED57A47FF8B53866542ED679AE1A68CB5433226AD3FC48A03E190C57AE0F27B44213B40CA3ECB39954DB4B58D7A9DB0E1E532DF5621B99B0F4EBF54C7A6A5E36BB57FE38927B0B6034D16CEAFB65E4EC347F055D994C6105601C6EC06C79B350F573D9D705054A82019158E343E5F480BA202C1640A3021D8E73C857F9C39FBE4E57DC7ACFCDC6256A72F11312292F406442DCE8B2846CA2299FC694FC1CA",
"serverId":    "3232",
"sig": "260fd4a42ce85eabf868401739334785",
"wi":  "1",
"areaName":    "安卓",
"nickname":    " 　ZWNR",
"qi":  "1",
"toServerId":  "3232",
"modulename":  "herolist",
"uin": "oFhrwsxpwaJp2xvgraEIcSKZVC-A",
"roleLevel":   "30",
"sourcePath":  "/data/user/0/com.tencent.gamehelper.smoba/files/hippy/herolist/34/index.android.jsbundle",
"algorithm":   "v2",
"timestamp":   "1595136697810",
"toAreaId":    "3",
"gameId":  "20001",
"toGameOpenId":    "owanlsjhh7xRwCKkzW6G_F7fqKIs",
"toAppRoleId": "2386193908",
"roleId":  "242079734",
"openid":  "oFhrwsxpwaJp2xvgraEIcSKZVC-A",
"env": "https://ssl.kohsocialapp.qq.com:10001",
"appVersionName":  "4.53.409",
"userId":  "1886577950",
"version": "3.1.96a",
"gameOpenid":  "owanlsjhh7xRwCKkzW6G_F7fqKIs",
"isMainRole":  "1",
"Brand":   "Xiaomi MI 8$",
"appOpenid":   "oFhrwsxpwaJp2xvgraEIcSKZVC-A",
"areaId":  "3",
"zn":  "安卓微信222区",
"platid":  "1",
"toAppOpenId": "oFhrwsxpwaJp2xvgraEIcSKZVC-A",
"roleJob": "永恒钻石II",
"appid":   "wxf4b1e8a3e9aaf978",
"roleName":    "清兵啊别打团",
"toGameRoleId":    "242079734",
"z":   "3232",
"__instanceName__":    "herolist",
"__instanceId__":  "10",
"gameOpenId":  "owanlsjhh7xRwCKkzW6G_F7fqKIs",
"fromType":    "1",
"uniqueRoleId":    "2386193908",
"msdkToken":   "[2Pmev3L7]"}
proxies = {
  "https": "http://localhost:8888",
}
store = []

# params 接收一个字典或者字符串的查询参数，字典类型自动转换为url编码，不需要urlencode()

response = requests.post("https://ssl.kohsocialapp.qq.com:10001/play/h5getherolist", params, headers = headers,verify=False,proxies=proxies)
js = response.json()
heros = js['data']
print(heros)
filename='heroall.json'
herojs="herojs.json"
herojson = {}
with open(filename,'w') as file_obj:
    json.dump(heros,file_obj)
for i in heros['heroList']:
    herojson[i['heroId']] = i['name']
print(herojson)
with open(herojs,'w') as file_obj:
    json.dump(herojson,file_obj)
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
