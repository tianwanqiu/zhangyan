"""
数字的阶层
"""


def get_jiecheng(number):
    result = 1
    while number > 1:
        result *= number
        number -= 1
    return result


print("jicheng 3 = %d" % (get_jiecheng(3)))

print("jicheng 6 = %d" % (get_jiecheng(6)))