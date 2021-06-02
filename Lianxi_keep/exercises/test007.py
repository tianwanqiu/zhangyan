"""
暂停一秒输出，并格式化当前时间
"""

import time


def method001():
    print(time.strftime('%Y-%m-%d %H:%M:%S'))
    time.sleep(1)
    print(time.strftime('%Y-%m-%d %H:%M:%S'))


if __name__ == "__main__":
    method001()
