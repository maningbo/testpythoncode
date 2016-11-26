#coding:utf-8
'''
Created on 2016年11月26日 下午4:07:38

@author: maningbo
'''

from datetime import timedelta,date
import time,datetime
from calendar import monthrange

if __name__=='__main__':
    print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())#当前时间
    print str(datetime.datetime.now())[0:19] #当前时间
    print datetime.datetime.now() #精确到微秒的当前时间
    print datetime.datetime.now().microsecond #当前时间的微秒数
    print int(time.time()) #当前时间的UNIX时间戳
    dateStr='2016-03-24'
    timestamp = int(time.mktime(time.strptime(str(dateStr), "%Y-%m-%d")))#字符串转时间戳
    print dateStr
    print timestamp
    print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(timestamp))#时间戳转字符串
    timesplit=dateStr.split("-")
    day=date(int(timesplit[0]),int(timesplit[1]),int(timesplit[2]))
    goal = timedelta(days=-10)
    goalday = day + goal
    data=goalday.strftime('%Y-%m-%d')
    print data
    
    monthlater = day + timedelta(days=monthrange(day.year,day.month)[1])
    print monthlater.strftime('%Y-%m-%d')
    print '-----------------------------------------------------'
    dt2='2016-04-01'
    timestamp2 = int(time.mktime(time.strptime(str(dateStr), "%Y-%m-%d")))
    print dt2
    print timestamp2
    timesplit2=dt2.split("-")
    day2 = date(int(timesplit2[0]),int(timesplit2[1]),int(timesplit2[2]))
    goal2 = timedelta(days=-1)
    goalday2 = day2 + goal2
    data2=goalday2.strftime('%Y-%m')
    print data2+'-01'