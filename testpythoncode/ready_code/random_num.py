#coding:utf-8
'''
Created on 2016年11月26日 下午3:09:11
参考链接：http://www.jb51.net/article/45653.htm
@author: maningbo
'''

import random

#uniform用于生成一个指定范围内的随机符点数，两个参数其中一个是上限，一个是下限
print random.uniform(10, 20)
print random.uniform(20, 10)
#randint用于生成一个指定范围内的整数，其中第一个参数是下限，第二个参数上限
print random.randint(12, 20) #生成的随机数n: 12 <= n <= 20 
print random.randint(20, 20) #结果永远是20 
# print random.randint(20, 10) #该语句是错误的。 