import threading
import time


def chi(threadName, name):
    print("%s开始吃%s" % (time.ctime(), threadName))
    time.sleep(1)
    print("%s吃火锅：涮羊肉" % time.ctime())
    time.sleep(1)
    print("%s吃火锅：涮牛肉" % time.ctime())
    time.sleep(1)
    print("%s吃火锅：涮贡丸" % time.ctime())
    time.sleep(1)
    print("%s吃%s结束---" % (time.ctime(), name))


def sing(threadName):
    print("%s开始唱%s" % (time.ctime(), threadName))
    time.sleep(1)
    print("%s唱小曲1" % time.ctime())
    time.sleep(1)
    print("%s唱小曲2" % time.ctime())
    time.sleep(1)
    print("%s唱小曲3" % time.ctime())
    time.sleep(1)
    print("%s唱%s结束---" % (time.ctime(), threadName))


# 定义线程组
threads = []
# 创建线程实例，target需要跑线程的函数，kwargs给函数传的值
t1 = threading.Thread(target=chi, kwargs={"threadName": "火锅", "name": "小火锅"})
threads.append(t1)

t2 = threading.Thread(target=sing, args=("唱歌",))
threads.append(t2)

if __name__ == "__main__":
    for i in threads:
        # 运行线程
        i.start()
