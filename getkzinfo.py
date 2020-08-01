import json
json_ob = {}
with open("heroextrainfos.json", "r") as f:
    for ov in f :
        ov = json.loads(ov.strip())
        json_ob = ov
heroname = input("对面啥英雄: ")
for i in json_ob:
    if(heroname in i['heroName']):
        print(i["heroName"]+"被:")
        for j in i['bkzInfo']['list']:
            print(j['szTitle']+j['bkzParam'])
        print("克制")
