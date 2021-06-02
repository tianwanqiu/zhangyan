"""
利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示
"""


def method001():
    score = float(input("请输入学生的成绩："))
    if score >= 90:
        print("学生成绩为A")
    elif (score >= 60) and (score < 90):
        print("学生成绩为B")
    else:
        print("学生成绩为C")


if __name__ == "__main__":
    method001()
