"""
python爬虫beautifulsoup框架可以解析html页面，最近看到lxml框架的语法更简洁，学过xpath定位的，可以立马上手
xpath   //标签和@属性
print(block[0].tag) 获取当前节点的标签
print(block[0].text) 获取当前节点的文本
print(block[0].attrib) 获取当前节点元素全部属性dict
print(block[0].xpath('text()')) 获取当前节点下全部文本
print(block[0].xpath('.//text()')) 获取本节点和子节点所有文本信息
"""
import requests
from lxml import etree
import lxml.html.soupparser as soupparser
import urllib3

# 禁用警告
urllib3.disable_warnings()


def pa():
    # 请求地址
    url = "https://www.cnblogs.com/yoyoketang/ajax/news.aspx"
    r = requests.get(url, verify=False)
    # print(r.text)
    # etree.HTML解析html 内容, soupparser解析器比上面的etree.HTML容错性要好一点，因为其处理不规范的html的能力比etree强太多。
    # dom = etree.HTML(r.content.decode("utf-8"))
    dom = soupparser.fromstring(r.content.decode("utf-8"))
    # 使用xpath 定位到想要获取的元素点
    block = dom.xpath("//*[@id='profile_block']")
    # t = etree.tostring(block[0],encoding="utf-8",pretty_print=True)
    # print(t.decode("utf-8"))
    t1 = block[0].xpath('text()')  # 获取当前节点的文本元素，以列表的方式呈现
    print(t1)
    t2 = block[0].xpath('a')  # 定位到 a 标签
    for i, j in zip(t1, t2):
        print("%s%s" % (i, j.text))
    print(block[0].xpath('.//text()'))


if __name__ == "__main__":
    pa()
