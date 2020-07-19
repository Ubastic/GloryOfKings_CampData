import json
import csv
import sys
with open("historyall.json", "r") as f:
    for ov in f :
        ov = json.loads(ov.strip())
        json_ob = ov
expand = []
for t in json_ob:
    for i in t:
        expand.append(i)
with open("detailsum.json", "r") as f:
    for ov in f :
        ov = json.loads(ov.strip())
        json_ov = ov
index=0
for v in expand:
    if(v==[]):
        continue
    for index,t in enumerate(json_ov):
        if('h5TeamAnaParam' in t):
            if(t['h5TeamAnaParam']['gameSeq'] == v['gameSeq'] ):
                json_ov[index]['win'] = "win" if v['gameresult']=="1" else "lose"
                if(t['eolType']=="掉分局"):
                    json_ov[index]['eolRight'] = "true" if json_ov[index]['win']=="lose" else "false"
                elif(t['eolType']=="上分局"):
                    json_ov[index]['eolRight'] = "true" if json_ov[index]['win']=="win" else "false"
                print(json_ov[index]['win'])
addwin = "detailwin.json"
with open(addwin,'w') as file_obj:
    json.dump(json_ov,file_obj)
    #if(v['gameSeq']!=json_ov[index]['h5TeamAnaParam']['gameSeq']):
        #print(v['gameSeq']+" "+json_ov[index]['h5TeamAnaParam']['gameSeq'])
        #print()
    #    continue
    #index+=1
    #json_ov[index]['win'] = "win" if v['gameresult']=="1" else "lose"
    #print(json_ov[index]['win'])
