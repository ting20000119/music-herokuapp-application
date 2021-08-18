import requests
from lxml import etree
res = requests.get(
    "https://zh.wikipedia.org/wiki/%E9%98%B2%E5%BD%88%E5%B0%91%E5%B9%B4%E5%9C%98%E9%9F%B3%E6%A8%82%E4%BD%9C%E5%93%81%E5%88%97%E8%A1%A8")
content = res.content.decode()  # 解析內容 (轉為string)
# print(content)
html = etree.HTML(content)  # 把string轉為hmtl node tree，回傳根節點
# date = html.xpath(
# "//table[@class='wikitable'][1]//tbody//tr[2]/td[2]/ul/li[1]/text()")  # //相對路徑 /絕對路徑
#b = html.xpath("//table[@class='wikitable'][1]//tbody//tr[3]/td[2]/ul/li[1]/text()")

for i in range(2, 6):
    date = html.xpath(
        "//table[@class='wikitable'][1]//tbody//tr[%d]/td[2]/ul/li[1]/text()" % (i))
    print(date)
    album_name = html.xpath(
        "//table[@class='wikitable'][1]//tbody//tr[%d]/td[2]/b/a/text()" % (i))
    print(album_name)
    song = html.xpath(
        "//table[@class='wikitable'][1]//tbody//tr[%d]/td[3]//div/ol/li//text()" % (i))
    list = [l.replace('\xa0', ' ') for l in song]
    print(list)
    print(len(song))

for i in range(2, 9):
    date = html.xpath(
        "//table[@class='wikitable'][2]//tbody//tr[%d]/td[2]/ul/li[1]/text()" % (i))
    print(date)
    album_name = html.xpath(
        "//table[@class='wikitable'][2]//tbody//tr[%d]/td[2]/b/a/text()" % (i))
    print(album_name)
    song = html.xpath(
        "//table[@class='wikitable'][2]//tbody//tr[%d]/td[3]//div/ol/li//text()" % (i))
    list = [l.replace('\xa0', ' ') for l in song]
    print(list)
    print(len(song))

for i in range(2, 6):
    date = html.xpath(
        "//table[@class='wikitable'][3]//tbody//tr[%d]/td[2]/ul/li[1]/text()" % (i))
    print(date)
    album_name = html.xpath(
        "//table[@class='wikitable'][3]//tbody//tr[%d]/td[2]/b/a/text()" % (i))
    print(album_name)
    song = html.xpath(
        "//table[@class='wikitable'][3]//tbody//tr[%d]/td[3]//div/ol/li//text()" % (i))
    list = [l.replace('\xa0', ' ') for l in song]
    print(list)
    print(len(song))

for i in range(2, 3):
    date = html.xpath(
        "//table[@class='wikitable'][4]//tbody//tr[%d]/td[2]/ul/li[1]/text()" % (i))
    print(date)
    album_name = html.xpath(
        "//table[@class='wikitable'][4]//tbody//tr[%d]/td[2]/b/a/text()" % (i))
    print(album_name)
    song = html.xpath(
        "//table[@class='wikitable'][4]//tbody//tr[%d]/td[3]//div/ol/li//text()" % (i))
    list = [l.replace('\xa0', ' ') for l in song]
    print(list)
    print(len(song))
