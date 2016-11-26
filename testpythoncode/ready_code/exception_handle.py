#coding:utf-8
'''
Created on 2016年11月26日 下午3:53:27

@author: maningbo
'''

if __name__=='__main__':
    try:
        raise Exception("出现异常了")
    except Exception,e:
        print e
        print str(e)+"11"