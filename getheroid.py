
# -*- coding:utf-8  -*-
import requests
import json
import sys
import time
headers = {
"accept":  "application/json, text/plain, */*",
"origin":  "https://image.ttwz.qq.com",
"user-agent":  "Mozilla/5.0 (Linux; Android 9.0; MI 8 Build/PKQ1.180729.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/044329 Mobile Safari/537.36;GameHelper; smobagamehelper; Brand: Xiaomi MI 8$",
"content-type":    "application/x-www-form-urlencoded",
"referer": "https://image.ttwz.qq.com/h5/webdist/hero-detail.html?heroid=184&appVersion=2020453409&role=%E6%B8%85%E5%85%B5%E5%95%8A%E5%88%AB%E6%89%93%E5%9B%A2&toOpenid=owanlsjhh7xRwCKkzW6G_F7fqKIs&serverName=%E5%BE%AE%E4%BF%A1222%E5%8C%BA&serverId=3232&wi=1&areaName=%E5%AE%89%E5%8D%93&nickname=%C2%A0%E3%80%80ZWNR&qi=1&roleLevel=30&gameId=20001&roleId=242079734&uniqueRoleId=2386193908&appVersionName=4.53.409&userId=1886577950&gameOpenid=owanlsjhh7xRwCKkzW6G_F7fqKIs&token=Ckk6THkG&isMainRole=1&appOpenid=oFhrwsxpwaJp2xvgraEIcSKZVC-A&areaId=3&zn=%E5%AE%89%E5%8D%93%E5%BE%AE%E4%BF%A1222%E5%8C%BA&platid=1&roleJob=%E8%87%B3%E5%B0%8A%E6%98%9F%E8%80%80IV&roleName=%E6%B8%85%E5%85%B5%E5%95%8A%E5%88%AB%E6%89%93%E5%9B%A2&z=3232&algorithm=v2&appid=wxf4b1e8a3e9aaf978&encode=2&openid=oFhrwsxpwaJp2xvgraEIcSKZVC-A&sig=0a370337adef90b1d338fcf0ee5c4e2d&source=smoba_zhushou&timestamp=1596279014546&version=3.1.96a&msdkEncodeParam=BCC6F0DC67794BFC98D10B0D3F66E14DC4C518040E9C53CFF0588C6340EB469F6295F40EA397372DAB3FEB04B3991E65C7368A52D426C931869031C3BE763C2D7555C732E2EFE67A61A0F3B9F8CFF3E0B243DFE12C542D7F12A2965677DA6EEE3EDF7147F7443D98559848425E57FB45BA5C414F4BCEAAA91F26DAF5903DB4D14491AA6C36A441C4BB91A82ECAE262B8C6FE384E58BBAF49E50DB21C427F2C6BD8F473D8D2DB9A7EE03E09FC1F4E52430C75685670CC37EB348C05768F85C80F6A636B99BBF7C3B6189B22C2742BFE80AE961D608C7E2BBCEC21B8526A2866008224EFC8F486639851BFB1B5644CB27D3432ACCB43BA86C0280CE16428B912967AB5758E449091D1776A1D801F5A720CBCC9C064B19CAE550AABB666FDE02364BEE96834B48D27E7ADA18C34604DFEC4ACA7AEBB6FD47787B6453B61BEE009546A33BC60FCE5369FA204CEF8DA78D1CAC60B8B9430D99CAF",
"accept-encoding": "gzip, deflate",
"accept-language": "zh-CN,en-US;q=0.8",
"x-requested-with":    "com.tencent.gamehelper.smoba",
"q-ua2":   "QV=3&PL=ADR&PR=TRD&PP=com.tencent.gamehelper.smoba&PPVN=4.53.409&TBSVC=43697&CO=BK&COVC=044329&PB=GE&VE=GA&DE=PHONE&CHID=0&LCID=9422&MO= MI8 &RL=1080*2028&OS=9&API=28",
"q-guid":  "20ea838fc9e72cfe8f8faaee1d0688cb",
"q-auth":  "31045b957cf33acf31e40be2f3e71c5217597676a9729f1b",
}
params = {"isNavigationBarHidden":   "1",
"appVersion":  "2020453409",
"role":    "%E6%B8%85%E5%85%B5%E5%95%8A%E5%88%AB%E6%89%93%E5%9B%A2",
"toOpenid":    "owanlsjhh7xRwCKkzW6G_F7fqKIs",
"serverName":  "%E5%BE%AE%E4%BF%A1222%E5%8C%BA",
"serverId":    "3232",
"wi":  "1",
"areaName":    "%E5%AE%89%E5%8D%93",
"nickname":    "%C2%A0%E3%80%80ZWNR",
"qi":  "1",
"roleLevel":   "30",
"gameId":  "20001",
"roleId":  "242079734",
"uniqueRoleId":    "2386193908",
"appVersionName":  "4.53.409",
"userId":  "1886577950",
"gameOpenid":  "owanlsjhh7xRwCKkzW6G_F7fqKIs",
"token":   "Ckk6THkG",
"isMainRole":  "1",
"appOpenid":   "oFhrwsxpwaJp2xvgraEIcSKZVC-A",
"areaId":  "3",
"zn":  "%E5%AE%89%E5%8D%93%E5%BE%AE%E4%BF%A1222%E5%8C%BA",
"platid":  "1",
"roleJob": "%E8%87%B3%E5%B0%8A%E6%98%9F%E8%80%80IV",
"roleName":    "%E6%B8%85%E5%85%B5%E5%95%8A%E5%88%AB%E6%89%93%E5%9B%A2",
"z":   "3232",
"algorithm":   "v2",
"appid":   "wxf4b1e8a3e9aaf978",
"encode":  "2",
"openid":  "oFhrwsxpwaJp2xvgraEIcSKZVC-A",
"sig": "e8fc7fc145ac42c23c9897a8f25ee3d5",
"source":  "smoba_zhushou",
"timestamp":   "1596279900625",
"version": "3.1.96a",
"msdkEncodeParam": "03C79DB383F016E6D7ECC2743ED0C6AC077E31A7721D50062A93EE90C76C9266EC3EC09E4FEEA2DC92788CBDC711164B5DAE8FEDDB21CD32E65F2A3129C8CB433AFA77F4E759ED3896E93B5B80DAB6D1C0E250BB4EBDB2A6ADC7637A30E6B95FB6D97D8850181441A93E2D69A3AA6787B411485D835FB17C5927E7235AE01609CBC4C524BE9B7F7EAA88313F9EF447FE8481F9E4B0CF487FBAA0EF1419FA2BB50B2CE0BFEA9A6C12A111AB9FCC786B5C145558915B7750F8C0781FC9D9129FF27984734E43C2D69D695355898590E42511A178721A2B0288ABF881DF23E4CAB20429136129FED9CFCC40FC45B6ECC87CF9079CE5234965A2E335923087233FFCC3C7D8E8653139FEB4DEF1306C1D42153C21CB0AE4815576F77E60B1DF78A3535F20BF143D2C8CE1EA162F518434A9CB6A2A86A5DD9A37843B17E53A248C1BE4085940CBA85D77CED955D294A95368C4B562E17BF03E5217",
"gameOpenId":  "owanlsjhh7xRwCKkzW6G_F7fqKIs",
"rankId":  "0",
"career":  "0",
"position":    "0",
"ifPeak":  "0",
"cSystem": "android",
"msdkToken":   "XOfmaoRV",
"h5Get":   "1"}


proxies = {
  "https": "http://localhost:8888",
}
store = []

response = requests.post("https://ssl.kohsocialapp.qq.com:10001/hero/getdetailranklistbyid", params, headers = headers,verify=False,proxies=proxies)
js = response.json()
if(js['result']==0):
    store.append(js['data']['list'])
    print(js['data']['title'])
filename='heroids.json'
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
