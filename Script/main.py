# -*- coding: utf-8 -*-
# @author: 橘子派
# @version: 2019-06-02 17:02:13
# 爬取妹子图片
# http://m.xingmeng365.com
# http://m.xingmeng365.com/articles.asp?id=2
# http://m.xingmeng365.com/articles.asp?id=1394
# http://m.xingmeng365.com/articles.asp?id=1394&mm=2
# http://img.xingmeng365.com//upload/image/20190610/20190610212229842984.jpg
# 存储文件地址为 './photo/'


import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    # photo的主地址
    photo_url = "http://m.xingmeng365.com/articles.asp?id="
    page_number = 1395
    index_number = 0
    photoName = ""
    while page_number > 1394:
        while index_number < 70:
            try:
                # 定义爬虫目标网站地址，第一张图和第二张图及其之后URL地址格式不一
                if index_number == 0:
                    url = 'http://m.xingmeng365.com/articles.asp?id=' + str(page_number)
                else:
                    url = 'http://m.xingmeng365.com/articles.asp?id=' + str(page_number) + "&mm=" + str(index_number)
                # 定义浏览器标头
                headers = {'user-agent': 'my-app/0.0.1'}
                r = requests.get(url, headers=headers)
                # 解决中文乱码问题
                r.encoding = 'gb18030'
                # 获得目标页面返回信息
                # print(r.status_code)
                print(url)
                if r.status_code == 500:
                    break
                if r.status_code == 200:
                    # 返回的信息放入soup中
                    # 获取页面全部标签信息
                    soup = BeautifulSoup(r.text, 'html.parser')
                    # print(soup.prettify())
                    # 测试显示的是否是页面的标签
                    for link in soup.find_all(name='h1'):
                        photoName = str(link).replace("<h1>", "").replace("</h1>", "")
                    for link in soup.find_all(name='img'):
                        # 输出图片地址
                        if str(link.get('src'))[:4] == 'http':
                            print(str(link.get('src')))
                            imageUrl = str(link.get('src'))
                            # 下载图片到photo文件夹中
                            response = requests.get(imageUrl)
                            with open('./photo/' + photoName + str(page_number) + '_' + str(index_number) + '.jpg', 'wb') as f:
                                f.write(response.content)
                index_number = index_number + 1
            except Exception as e:
                index_number = index_number + 1
                print(e)
        page_number = page_number - 1
        index_number = 0
