从王者营地获取王者荣耀近一个月的对战数据，根据英雄战力看看有没有什么被安排的可能。
营地的list是一个月，但是detail更久远，可以先爬list。
目前结果大失所望，如果只看战斗力，只有50%的安排成功率，王者具体算法依然未知，如果用elo、MMR算法一个个算，爬的东西太多了。
list 1 month, but detail save permanently in server. so just need to get detail number
部分用户关闭权限，无法获得战力，但是有熟练英雄的战力数据可供参考，以及段位、胜率等。

王者小程序数据过于少，没有什么价值。

这个爬虫项目比较久远，王者营地的api可能会变更，主要是用charles抓包，获取headers。
爬虫是playdetail.py和playhistory.py两个文件，herolist.py可以获取所有英雄数据，主要是找英雄和他们的id。
其他文件是对爬下来的json进行处理，这部分就看你想要获得什么了。
