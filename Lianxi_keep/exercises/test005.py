"""
将一个列表的数据复制到另一个列表中
复制即为深拷贝和浅拷贝
"""


def method001():
    list1 = list(range(10))
    # 深拷贝
    list2 = list1
    print(list2)

    # 浅拷贝
    list3 = list1[:]
    print(list3)

    # 浅拷贝
    list4 = list1.copy()
    print(list4)


if __name__ == "__main__":
    method001()
