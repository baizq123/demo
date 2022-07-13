#!/usr/bin/python3
# --coding:utf-8--
# @File:aaa.py
# @Author:baizq

# import os
# def du_xie_txt(filename):
#     with open(rf'./rtf/{filename}','r') as f:
#         shuju = f.readlines()
#     shuj = []
#     for k,j in enumerate(shuju):
#         if 'Filename:' in j:
#             shuj.append(j)
#         elif 'Report Generated On' in j:
#             shuj.append(j)
#         elif 'IDENTIFIED NUCLIDES' in j:
#             # print(k,j)
#             shuj.append(k)
#
#     with open('aa.txt','a',encoding='utf-8') as f:
#         for i in shuj:
#             try:
#                 f.write(i)
#             except:
#                 for j in range(i,len(shuju)):
#                     if '* = Energy line found in the spectrum.' in shuju[j]:
#                         k = j
#                         break
#                 for kk in range(i,k):
#                     f.write(shuju[kk])
#
# def du_xie_rtf(filename):
#     with open(rf'./rtf/{filename}','r') as f:
#         dat = f.readlines()
#
#     with open('aa.rtf','a',encoding='utf-8') as f:
#         for i,j in enumerate(dat):
#             if 'S#' in j:
#                 f.write(''.join(dat[i:]))
#
# def du_xie_rpt(filename):
#     with open(rf'./rtf/{filename}','r') as f:
#         dat = f.readlines()
#
#     shuj = []
#     for k,j in enumerate(dat):
#         if '能谱文件: E:' in j:
#             shuj.append(j.strip())
#         elif '开始时间' in j:
#             shuj.append(j.strip())
#         elif '样 品 中 核 素 一 览 表' in j:
#             shuj.append(k)
#
#     with open('aa.rpt','a',encoding='utf-8') as f:
#         for i in shuj:
#             try:
#                 f.write(i+'\n')
#             except:
#                 for j in range(i,len(dat)):
#                     if '< - 报告的活度是最小可探测活度(MDA).' in dat[j]:
#                         k = j
#                         break
#                 for kk in range(i,k):
#                     f.write(dat[kk])
#
#
# # 过滤文件
# dir = os.listdir(r'./rtf')   # 存放文件的目录
# for i in dir:
#     if '.txt' in i:
#         du_xie_txt(i)
#     elif '.rtf' in i:
#         du_xie_rtf(i)
#     else:
#         du_xie_rpt(i)








# import requests
# import json
# import threading
#
# # url = "http://lql-api-purchase.dev_golang.91quliao.com/gift/brush"
# # data = {
# #     "toUserId":"2021037",
# #     "scene":"live_gift",
# #     "groupId":"2021037",
# #     "giftId":"612ded0635c7a25de483cf4f",
# #     "giftNum":1
# #     }
#
# import requests
# import threading
# import json
#
#
# head = {"content-type":"application/json",
#         "token":"cef72c838e26d0152e1d43e2b02b907a4d8e743f63cb4db1f076f7acc17204faceca2afe03425e520f3ff240b022d33c69de18b451a6c0b614a2ee564974e8d78c65a8f49e3bf5880e738ede35775518"}
#
#
# def gailv(url,data):
#     daa = json.dumps(data)
#     res = requests.post(url,headers=head,data=daa)
#     html = res.json()
#     print(html)
#     return html
#
#
# url = "http://lql-api-purchase.dev_golang.91quliao.com"
# songli = "/gift/brush"
# data = {
#     "toUserId":"2021037",
#     "scene":"live_gift",
#     "groupId":"2021037",
#     "giftId":"618a392e88579c8de0e3b367",
#     "giftNum":1
#     }
#
# for i in range(1000000):
#     pass
#
#
# mingxi = "/wallet/details"
# qury = "page=1&size=9999999&month=202111"
# res = requests.get(url+mingxi,headers=head,params=qury).json()
# print(res)










# list = []
# new_list = []
# def guolv(html):
#     shuju = html["openData"]["multiplyRate"]
#     if shuju in list:
#         new_list.append(shuju)
#     else:
#         list.append(shuju)
#         new_list.append(shuju)
#
# url = "http://cwl-api-activity.dev_golang.91quliao.com/activity/turntable/play"
# data = {"num":100}
#
#
# for k in range(100):
#     html = gailv(url,data)
#     guolv(html)
#
# for i in list:
#     aa = 0
#     for j in new_list:
#         if i == j:
#             aa += 1
#     print(f"{i}:{aa}")
#



























































import requests
import hashlib
import random
import json
from time import sleep

def rand():
	abc = []
	for i in range(8):
		abc.append(str(random.randint(0,9)))
	return ''.join(abc)

def post_sign(bb):
	res = bb.lower()
	abc = ''.join(sorted(res))
	abc += "lAEhdjtiRbuq2owpi0g5Lm2z6iLbcfbm"
	m = hashlib.md5()
	m.update(abc.encode())
	return m.hexdigest()

def zhuce(envir):
	url = f"http://user.test{envir}golang.91quliao.com/user/login/sms"
	# url = "http://lql-api-user.dev_golang.91quliao.com/user/login/sms"
	daa = {
		"mobile":f"175{rand()}",
		"code":"123456",
		"type":"login"
		}
	daa = json.dumps(daa)
	daaa = post_sign(daa)
	head = {"sign": daaa}
	res = requests.post(url,data=daa,headers=head).json()
	return res["openData"]["token"]


def wanshan(tok,i,envir):
	url = f"http://user.test{envir}golang.91quliao.com/user/login/info"
	# url = "http://lql-api-user.dev_golang.91quliao.com/user/login/info"
	daa = {
		"gender": "female","born": "2000-01-02","starSign": "白羊座","nickName": "xin%s"%(i)
		}
	daa = json.dumps(daa)
	daaa = post_sign(daa)
	head = {"content-type":"application/json","token":"%s"%(tok),"sign": daaa}
	res = requests.post(url,data=daa,headers=head).json()

def my(tok,envir):
	url = f"http://user.test{envir}golang.91quliao.com/user/my"
	# url = "http://lql-api-user.dev_golang.91quliao.com/user/my"
	head = {"token":"%s"%(tok)}
	res = requests.get(url,headers=head).json()
	return res["openData"]["noId"]

def 创建账号(envir):
	with open("ee.txt",'w',encoding='utf-8') as f:
		for i in range(50):
			tok = zhuce(envir)
			wanshan(tok,i,envir)
			noid = my(tok,envir)
			f.write(f"{noid},{tok}"+'\n')

def post_sign_web(bb):
	res = bb.lower()
	abc = ''.join(sorted(res))
	abc += "PGncRld3YLMdF9bRlvFFgcW6Lm3rkHFk"
	m = hashlib.md5()
	m.update(abc.encode())
	return m.hexdigest()

def get_sign(get_qury):
	res = get_qury.replace('=', '').replace('&', '')
	res = res.lower()
	res = ''.join(sorted(res))
	res = res + "PGncRld3YLMdF9bRlvFFgcW6Lm3rkHFk"
	m = hashlib.md5()
	m.update(res.encode())
	return m.hexdigest()

def chaxun(noid,envir):
	url = f"http://adminzt.test{envir}golang.91quliao.com/user/query?noId={noid}"
	qury = url.split('?')[1]
	# s = Sign("lAEhdjtiRbuq2owpi0g5Lm2z6iLbcfbm","PGncRld3YLMdF9bRlvFFgcW6Lm3rkHFk")
	# sign = s.get_web(url)
	# print(ss)
	daaa = get_sign(qury)
	head = {"sign": daaa,"platform":"web","token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhZG1pblVzZXJJZCI6IjYxNzkwYjI2ZTgxNzViZjA3Y2E0OWZlNiIsIm5hbWUiOiJhZG1pbiIsIm1vYmlsZSI6IjE4OTg5ODI1NTMyIn0.2QdvMYQ1zRf21kqJUNTv-TxXt9PtT5JZY1lO7f5uh8M"}
	res = requests.get(url,headers=head).json()
	return res

def chongzhi(id,envir):
	url = f"http://adminzt.test{envir}golang.91quliao.com/account/currencyConfig"
	daa = {"uid":"%s"%(id),"amount": 5000000000, "currencyType": "diamonds", "opType": "add"}
	daa = json.dumps(daa)
	daaa = post_sign_web(daa)
	head = {"sign": daaa,"platform":"web","token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhZG1pblVzZXJJZCI6IjYxNzkwYjI2ZTgxNzViZjA3Y2E0OWZlNiIsIm5hbWUiOiJhZG1pbiIsIm1vYmlsZSI6IjE4OTg5ODI1NTMyIn0.2QdvMYQ1zRf21kqJUNTv-TxXt9PtT5JZY1lO7f5uh8M"}
	res = requests.post(url,headers=head,data=daa)
	sleep(1)
	res.json()

def 充值(envir):
	with open('ee.txt','r',encoding='utf-8') as f:
		aa = f.readlines()
	for i in aa:
		i = i.split(',')
		id = chaxun(i[0],envir)
		# chongzhi(id)
		# for j in range(5):
		chongzhi(id["openData"]["base"]["userId"],envir)

创建账号("one")
充值("one")




# def reques(tok):
# 	url = "http://purchase.testtwogolang.91quliao.com/gift/brush"
# 	bb = {
# 	"giftId":"6125e569bb85b4493b32a9a4",
# 	"scene":"live_gift",
# 	"giftNum":1,
# 	"comboNum":2,
# 	"comboId":"37AE4BB3-84FD-4726-A1F6-E16F5FE22A0C",
# 	"groupId":22021135,
# 	"toUserId":22021135
# 	}
# 	daa = json.dumps(bb)
# 	daaa = post_sign(daa)
# 	head = {"content-type":"application/json","token":"%s"%(tok)}
# 	res = requests.post(url,headers=head,data=bb)
# 	print(res.json())
#
#
# with open('e.txt','r',encoding='utf-8') as f:
# 	aa = f.readlines()
#
# reques(aa[0][1])













# def 加密(abc):
# 	if "=" in abc:
# 		aa = abc.replace('=','')
# 		if "&" in "aa":
# 			bb = aa.replace('&','')
# 			cc = sorted(bb)
# 			dd = ''.join(cc)+"PGncRld3YLMdF9bRlvFFgcW6Lm3rkHFk"
# 			return dd
# 		else:
# 			cc = sorted(aa)
# 			return ''.join(cc)+"PGncRld3YLMdF9bRlvFFgcW6Lm3rkHFk"
# 	else:
# 		cc = sorted(abc)
# 		return ''.join(cc) + "PGncRld3YLMdF9bRlvFFgcW6Lm3rkHFk"
#
#
# def md5(info):
# 	m = hashlib.md5()
# 	m.update(info.encode())
# 	m.hexdigest()
# 	return m.hexdigest()

# info = 加密("noId=7778975")
# md5(info)


# f = open('a.txt','r')
# aa = f.readlines()
# f.close()

# for i in aa:
# 	i = i.split(',')
# 	id = chaxun(i[0])
# 	if id["openData"]["account"]["diamonds"] == 0:
# 		chongzhi(id["openData"]["base"]["userId"])

# for i in aa:
# 	i = i.split(',')
# 	wanshan(i[1].strip())

# f = open('a.txt','r')
# ff = f.readlines()
# f.close()

# f = open('b.txt','a',encoding='utf-8')
# for i,j in enumerate(ff):
# 	if i==50:
# 		break
# 	else:
# 		f.write(j)







