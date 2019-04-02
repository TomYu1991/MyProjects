#Author:Tom_Fish
#-*- coding:utf-8 -*-
import requests
from xml import etree
headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36'
        }
res = requests.get('http://kaijiang.500.com/shtml/dlt/18001.shtml', headers=headers)
html = etree.HTML(res.text)
result = etree.tostring(html)
print(result)
