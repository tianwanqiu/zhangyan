"""
多线程实战，使用tomorrow模块中的多线程方法 实现快速下载文件
BeautifulSoup 模块是python 用来专门解析 HTML 和 XML 的库
"""

from bs4 import BeautifulSoup
import os
import requests
import time
from tomorrow import threads

# 当前脚本所在的目录（是文件夹的目录）
cur_path = os.path.dirname(os.path.relpath(__file__))


def get_images_url():
    r = requests.get("http://699pic.com/sousuo-218808-13-1.html")
    fengjing = r.content
    # 解析获取的html 格式的返回值
    soup = BeautifulSoup(fengjing, "html.parser")
    # 找出所有标签
    images = soup.find_all(class_='lazy')
    return images


@threads(5)
def sav_image(image_url):
    try:
        jpg_url = image_url["data-original"]
        jpg_title = image_url["title"]
        # 创建jpg 文件夹
        save_file = os.path.join(cur_path, "jpg")
        if not os.path.exists(save_file):
            os.makedirs(save_file)
        with open(os.path.join(save_file, jpg_title + ".jpg"), "wb") as f:
            f.write(requests.get(jpg_url).content)
    except:
        pass


if __name__ == "__main__":
    t1 = time.time()

    image_urls = get_images_url()
    for i in image_urls:
        sav_image(i)

    t2 = time.time()
    print("总耗时：%2f 秒" % (t2 - t1))
