"""
经典面试题： 判断一个字符串里面的括号是否闭合
解决基本思路：先把左括号添加到一个列表里面，遇到右括号就弹出列表里面的最后一个存放进去的。
对比右括号和弹出的左括号是否对称，如果是就继续依次对比
最后判断列表里面是否有多余的左括号，如果列表为空，说明全部被弹出，那就是闭合的
"""


def is_str_close(a):
    b = []
    flag = True
    for i in a:
        # 将左边符号全部放到数组之中
        if i == "{" or i == "[" or i == "(":
            b.append(i)
        # 右边符号等于“）”时会去掉一个
        elif i == ")":
            if len(b) == 0 or b.pop() != "(":
                return False
        elif i == "]":
            if len(b) == 0 or b.pop() != "[":
                return False
        elif i == "}":
            if len(b) == 0 or b.pop() != "{":
                return False
    # 如果还有符号残留就不是闭合，返回 flase
    if len(b) != 0:
        flag = False
    return flag


if __name__ == "__main__":
    a = "{[{()}]()}"
    print(is_str_close(a))
    c = "{[{()}]()}]"
    print(is_str_close(c))
