#! /usr/bin/env python2.7
# -*- coding: UTF-8 -*-
# -*- coding: cp936 -*-
# -*- coding: gb18030 -*-


#--------------------------------------------------#
#     Author:guchao
#     mail  :guchaonemo@163.com
#     time  :2017.09.29 15:00
#     USAEG :download pm2.5 data
#--------------------------------------------------#

import sys
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd

reload(sys)
sys.setdefaultencoding("utf-8")


class PM2Nanjing(object):

    def __init__(self, url):
        self.url = url
        headers = {'Host': 'www.bjrbj.gov.cn',
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0',
                   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                   'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
                   'Accept-Encoding': 'gzip, deflate', 'Referer': 'http://www.bjrbj.gov.cn/csibiz/indinfo/top_ind.jsp'}
        Host = (url.split(':')[1][2:]).split('/')[0]
        headers['Host'] = Host
        headers['Referer'] = url
        self.headers = headers

    def loaddata(self):
        sess = requests.Session()
        req = sess.get(url, headers=self.headers)
        self.resolve(req.content)

    def resolve(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        table = soup.select('table')[0]
        lines = table.select('tr')
        result = []
        for i in range(1, 10):
            line = lines[i]
            line = [ele.string for ele in line.select('td')]
            #line = [ele.replace('<br/>', '|') for ele in line]
            result.append(line)
        df = pd.DataFrame(result)
        csvname = str(datetime.now().strftime("%Y-%m-%d %H-%M"))+".csv"
        df.to_csv(csvname, index=False, header=False, encoding="gb2312")


if __name__ == '__main__':
    url = 'http://www.pm25.in/nanjing'
    Loader = PM2Nanjing(url)
    Loader.loaddata()