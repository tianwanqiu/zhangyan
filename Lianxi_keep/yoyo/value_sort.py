"""
如何统计数组中出现次数最多的数据，按出现的次数由大到小排序
"""

a = ["a", "b", "a", "c", "a", "c", "b", "d", "e", "c", "a", "c"]


def paixu():
    # 对列表去重
    duixiang = set(a)
    print(duixiang)
    d = {}
    # 将某个字母对应统计的数值塞到字典中
    for i in duixiang:
        d[i] = a.count(i)
    print(d)
    # 将字典中数据按照 统计的数值 从大到小排序
    s = sorted(d.items(), key=lambda x: x[1], reverse=True)
    print(s)


if __name__ == "__main__":
    paixu()
