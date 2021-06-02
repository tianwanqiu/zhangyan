"""
发送邮件功能demo

公司邮箱无法设置 pop 和 smtp
"""

import zmail


def send_email():
    # 发送邮件的内容
    mail_content = {"subject": "测试邮件", "content_html": "测试邮件内容"}
    # 发送者邮箱
    server = zmail.server('13451845380@163.com', 'ZY@54321!')
    # 发送对象邮箱地址
    server.send_mail('547115506@qq.com', mail_content)


if __name__ == "__main__":
    send_email()
