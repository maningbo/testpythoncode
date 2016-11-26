#coding:utf-8
'''
Created on 2016年11月26日 下午4:01:29

@author: maningbo
'''

import sys

if __name__ == "__main__":
    print "地方"
    #防止中文时报错，开始
    reload(sys)
    sys.setdefaultencoding("utf8")
    #防止中文时报错，结束
    print "地方"