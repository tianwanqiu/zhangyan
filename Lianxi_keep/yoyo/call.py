"""
__call__()将类实例变为可调用对象
"""


class TestCall:

    def __init__(self, size, x, y):
        self.x = x
        self.y = y
        self.size = size

    def __call__(self, x, y):
        self.x = x
        self.y = y
        print(self.x)
        print(self.y)

    def sum(self):
        print(self.x + self.y)


if __name__ == "__main__":
    sc = TestCall(1, 2, 3)  # 实例化对象,实验证明这里的参数是必传的，因为__init__()方法中有此参数
    sc(4, 5)
    sc.sum()
