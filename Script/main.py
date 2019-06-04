# -*- coding: utf-8 -*-
# @author: 橘子派
# @version: 2019-06-02 17:02:13
# 爬取妹子图片
# http://m.xingmeng365.com
# http://m.xingmeng365.com/articles.asp?id=2
# http://m.xingmeng365.com/articles.asp?id=1387
# http://m.xingmeng365.com/articles.asp?id=1387&mm=2
# http://m.xingmeng365.com/upload/image/20190531/20190531221061596159.jpg
# 存储文件地址为 '../photo/'


import requests
from bs4 import BeautifulSoup
import urllib
import socket


# 回调函数
# @a:已经下载的数据块
# @b:数据块的大小
# @c:远程文件的大小
def cbk(a, b, c):
    per = 100.0 * a * b / c
    if per > 100:
        per = 100
    print('%.2f%%' % per)


if __name__ == '__main__':
    # photo的主地址
    photo_url = "http://m.xingmeng365.com/upload/"
    # 保存图片，XXXXX_index.jpg
    file = '../photo/'
    # page_number = 1387
    page_number = 3
    index_number = 3
    while page_number > 0:
        # while index_number < 70:
        while index_number > 0:
            try:
                # 定义爬虫目标网站地址
                if index_number == 0:
                    url = 'http://m.xingmeng365.com/articles.asp?id=' + str(page_number)
                else:
                    url = 'http://m.xingmeng365.com/articles.asp?id=' + str(page_number) + "&mm=" + str(index_number)
                # 定义浏览器标头
                headers = {'user-agent': 'my-app/0.0.1'}
                r = requests.get(url, headers=headers)
                # 获得目标页面返回信息
                print(r.status_code)
                print(url)
                while r.status_code == 200:
                    # 返回的信息放入soup中
                    # 获取页面全部标签信息
                    soup = BeautifulSoup(r.text, 'html.parser')
                    print(soup.prettify())
                    # 测试显示的是否是页面的标签
                    # for link in soup.find_all(img="div-num"):
                        # 输出图片地址
                        # print(link.get('data-src'))
                        # 设置超时
                        # socket.setdefaulttimeout(5.0)
                        # urllib.request.urlretrieve(link.get('data-src'),
                        #                            file + '/' + str(page_number) + '_' + str(index_number) + '.jpg', cbk)
                        # index_number = index_number - 1
                index_number = index_number - 1
            except Exception as e:
                index_number = index_number - 1
        page_number = page_number - 1
