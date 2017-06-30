#coding:utf-8
import requests
from config import *
import base

def edit(areacode, wenli = 2):
    body['ProvinceCode'] = areacode
    body['WenLi'] = wenli
    print requests.post(url=url, data=body, headers=header).content

if __name__ == "__main__":
    edit(410000)
    base.get_cookie()