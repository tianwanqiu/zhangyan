"""
求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制
"""


def method001():
    global s
    a = int(input("请输入a 的值："))
    num = int(input("请输入需要相加的数量："))
    s = a
    total = 0

    while num > 0:
        total += s
        s = s*10 + a
        num -= 1
    # 返回值一定要放在外面
    return total


if __name__ == "__main__":
    print(method001())
