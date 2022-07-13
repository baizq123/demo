#!/usr/bin/python3
# --coding:utf-8--
# @File:testcase.py
# @Author:baizq
import pytest
import allure
# from comman import du_api
# with open(r'../data/fenlei/充值.json', 'r') as f:
#     dat = f.readlines()
# #
# class Test_chong():
#     pass
#     # @pytest.mark.parametrize('x,y,z,q',(['1',2,3,4],['5',6,7,8]))
#     # def test_1(self,pa,x,y,z,q):
#     #     url = "http://www.baidu.com" + pa["path"]+x
#     #     if pa["method"] == "POST":
#     #         try:
#     #             body = du_api.c_body(pa["req_body_other"],(x,y,z,q))
#     #             head = du_api.c_head(pa["req_headers"])
#     #             res = du_api.qing_qiu().method_post(url, head=head, par=body)
#     #             print(head)
#     #             res = res.text
#     #         except:
#     #             head = du_api.c_head(pa["req_headers"])
#     #             res = du_api.qing_qiu().method_post(url, head=head)
#     #             res = res.text
#     #
#     #     else:
#     #         try:
#     #             head = du_api.c_head(pa["req_headers"])
#     #             qur = du_api.c_query(pa["req_query"])
#     #             res = du_api.qing_qiu().method_get(url,head=head,par=qur)
#     #             res = res.text
#     #         except:
#     #             head = du_api.c_head(pa["req_headers"])
#     #             res = du_api.qing_qiu().method_get(url, head=head)
#     #             res = res.text
#     #
#     #     assert "404" in res
#
#     # def test_a(self):
#     #     @allure.title("充值")
#     #     @allure.description("ios充值")
#
#
# if __name__ == "__main__":
#     pytest.main()
#
# import json
# with open(rf'D:\ruanjian\ap.json','r',encoding='utf-8') as f:
#     dat = f.read()
#     dat = json.loads(dat)
import json
from ruamel import yaml

with open(r'../data/fenlei/搜索.json','r') as f:
    dat = f.read()
    dat = json.loads(dat)

with open('aaa.yaml', "w") as f:
    yaml.dump(dat, f, Dumper=yaml.RoundTripDumper,default_flow_style=False,encoding='utf-8',allow_unicode=True)

with open('aaa.yaml','r') as f:
    dd = yaml.safe_load(f)
print(dd)