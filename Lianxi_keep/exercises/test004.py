"""
输入三个整数x,y,z，请把这三个数由小到大输出
"""


def method_001():
    l = []
    for i in range(3):
        x = int(input("请依次输入x,y,z的数值："))
        l.append(x)
    l.sort()
    print(l)


if __name__ == "__main__":
    method_001()
