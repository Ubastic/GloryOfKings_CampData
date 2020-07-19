import json
with open("detailall.json", "r") as f:
    for ov in f :
        ov = json.loads(ov.strip())
        json_ob = ov
with open("herojs.json", "r") as f:
    for ov in f :
        ov = json.loads(ov.strip())
        json_hero = ov
banlist={}
for i in json_ob:
    if('banHeroInfo' in i.keys()):
        if(i['banHeroInfo']!=[]):
            #print(i['banHeroInfo'])
            for t in i['banHeroInfo']['camp1']:
                if(t['heroId']=="0"): #沒禁
                    continue
                if(t['heroId'] not in banlist.keys()):
                    banlist[t['heroId']] = 0
                else:
                    banlist[t['heroId']] += 1
            for t in i['banHeroInfo']['camp2']:
                if(t['heroId']=="0"): #沒禁
                    continue
                if(t['heroId'] not in banlist.keys()):
                    banlist[t['heroId']] = 0
                else:
                    banlist[t['heroId']] += 1
#print(banlist)
banname = {}
for i in banlist.keys():
    #print(i)
#    print(json_hero[i])
    banname[json_hero[i]] = banlist[i]
    #banname[i] = {"banTime":banlist[i],"name":json_hero[i]}
print(banname)
bansort= sorted(banname.items(),key=lambda x:x[1],reverse=True)
for t in bansort:
    print(t[0]+":"+str(t[1]))
#print(bansort)
