"""
一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
我写的与案例的差别：没有做成可输入的，没有使用数组
"""


def method001():
    global a, s, c
    a = 200
    s = 100
    c = 100
    total = 0
    for i in range(1, 11):
        total += s
        s = a / 2
        a = a / 2
        c = c / 2
        if i == 10:
            print("第10次反弹高度:%.2f" % c)
            continue
    print("10次落地时共经过:%.2f" % total)


def method002():
    times = int(input("Hou many times the ball hit the floor?"))
    h = 100.0
    record = []
    length = 100
    for i in range(0, times):
        h = h / 2
        record.append(h)
    for i in record[:-1]:
        length += i * 2
    print(length)
    print(record[-1])


if __name__ == "__main__":
    method002()
