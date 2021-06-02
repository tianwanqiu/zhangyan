"""
python里面[]表示一个列表，快速生成一个列表可以用range()函数来生成。
对列表里面的数据进行运算和操作，生成新的列表最高效快速的办法，那就是列表生成式了
"""


def scs():
    a = []
    for i in range(1, 11):
        a.append(i)
    print(a)
    # 生成式用于运算
    b = [x * x for x in a]
    print(b)
    # 生成式带if 条件判断
    c = [x for x in b if x < 50]
    print(c)
    # 生成式多个参数,实现两个元素组合，x 在a 中循环；y 在b 中循环
    d = [str(x) + str(y) for x, y in zip(a, b)]
    print(d)


if __name__ == "__main__":
    scs()
