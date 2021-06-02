import queue
# 定义一个队列，最大长度为10
q = queue.Queue(maxsize=10)
for i in range(100):
    if q.qsize() >= 10:
        break
    else:
        q.put(i)
# 当队列不是空的时候一直取出
while not q.empty():
    n = q.get()
    print("本次取出数据：%s" % n)
