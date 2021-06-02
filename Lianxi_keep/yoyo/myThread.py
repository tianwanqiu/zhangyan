import threading
import time


def ChiHuoGuo(people):
    print("%s吃火锅--羊肉%s" % (time.ctime(), people))
    time.sleep(1)
    print("%s吃火锅--鱼丸%s" % (time.ctime(), people))


# 继承父类threading.Thread
class myThread(threading.Thread):
    def __init__(self, people, name):
        # 重写threading.Thread 中初始化方法
        threading.Thread.__init__(self)
        self.name = name
        self.people = people

    # 重写threading.Thread 中的run 方法，相当于线程中得target
    def run(self):
        print("开始线程:%s" % self.name)
        ChiHuoGuo(self.people)
        print("结束线程:%s" % self.name)


if __name__ == "__main__":
    t1 = myThread("xiaowang", "线程1")
    t2 = myThread("xiaozhang", "线程2")

    # 守护主线程：等所有的线程跑完之后才退出主线程，主线程结束了，子线程必须也跟着结束，只会跑一遍线程就结束
    t1.setDaemon(True)
    t2.setDaemon(True)

    t1.start()
    t2.start()
    # 阻塞主线程：会将函数里面的内容都执行完，才会去执行函数下面的内容
    # t1.join()
    # t2.join()
    print("退出主线程：吃火锅结束，结账走人")
