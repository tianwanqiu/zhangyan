"""
有5个人坐在一起，问第五个人多少岁？他说比第4个人大2岁。问第4个人岁数，他说比第3个人大2岁。
问第三个人，又说比第2人大两岁。问第2个人，说比第一个人大两岁。最后问第一个人，他说是10岁。请问第五个人多大？
思考：x-2-2-2-2=10
"""


def method001():
    f = 10
    li = [10]
    for i in range(1, 5):
        sui = f + 2
        f += 2
        li.append(sui)
    li.sort(reverse=True)
    print(li)


if __name__ == "__main__":
    method001()
