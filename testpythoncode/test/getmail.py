#coding:utf-8
'''
Created on 2016年9月11日
参考链接：http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001408244819215430d726128bf4fa78afe2890bec57736000
@author: maningbo
'''
import poplib
from email.parser import Parser

# 输入邮件地址, 口令和POP3服务器地址:
email = "0.000.0.0.0.0."
password = ".0.0.0.0.0..0"
pop3_server = "0.0.0.0.....00"

# 连接到POP3服务器:
server = poplib.POP3(pop3_server)
# 可以打开或关闭调试信息:
# server.set_debuglevel(1)
# 可选:打印POP3服务器的欢迎文字:
print(server.getwelcome())
# 身份认证:
server.user(email)
server.pass_(password)
# stat()返回邮件数量和占用空间:
print('Messages: %s. Size: %s' % server.stat())
# list()返回所有邮件的编号:
resp, mails, octets = server.list()
# 可以查看返回的列表类似['1 82923', '2 2184', ...]
print(mails)
# 获取最新一封邮件, 注意索引号从1开始:
index = len(mails)
resp, lines, octets = server.retr(index)
# lines存储了邮件的原始文本的每一行,
# 可以获得整个邮件的原始文本:
# msg_content = '\r\n'.join(lines)
# 稍后解析出邮件:
# msg = Parser().parsestr(msg_content)
# print msg
# 可以根据邮件索引号直接从服务器删除邮件:
# server.dele(index)
# 关闭连接:
server.quit()