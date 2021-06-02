"""
给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字
思考：字符串的倒序打印
"""


def method001():
    num = input("请输入一个不多于5位的正整数：")
    print(len(num))
    for i in range(len(num)-1, -1, -1):
        print(num[i])


if __name__ == "__main__":
    method001()
