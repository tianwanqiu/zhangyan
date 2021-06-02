"""
输入一行字符，分别统计出其中 英文字母、空格、数字和其它字符的个数。（不是中英文字符。。。。）
"""


def method001():
    s = input("请输入一个字符串")
    str = 0
    space = 0
    degit = 0
    others = 0
    for i in s:
        if i.isalpha():
            str += 1
        elif i.isspace():
            space += 1
        elif i.isdigit():
            degit += 1
        else:
            others += 1
    print("length=%d, char=%d, space=%d,degit=%d, others=%d " % (len(s), str, space, degit, others))


if __name__ == "__main__":
    method001()
