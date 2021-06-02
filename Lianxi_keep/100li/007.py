"""
计算数字范围类的所有偶数
"""

"""
def is_os(s):
    if s % 2 == 0:
        return True
    return False


def pr_os(a, n):
    for i in range(a, n + 1):
        if is_os(i):
            print(f"{i}是偶数") 
            # print(i)


pr_os(5, 11)
"""


def pr_os(begin, end):
    result = []
    for i in range(begin, end + 1):
        if i % 2 == 0:
            result.append(i)
    return result


print("偶数值列表为：", pr_os(5, 11))
