"""
一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同
"""


def method001():
    num = input("请输入一个5位数：")
    s = len(num)
    if s != 5:
        print("请输入5位数")
    elif (num[0] == num[4]) and (num[1] == num[3]):
        print("回文数")
    else:
        print("不是回文数")


def method002():
    num = input("请输入数值：")
    if num == num[::-1]:
        print("回文数")  # 利用str的[::-1] 的方法，正过来和反过来的数值一样
    else:
        print("不是回文数")


if __name__ == "__main__":
    method002()
