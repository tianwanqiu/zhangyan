import flask

# 创建接口后台服务，方便接口请求
# 把文件当成一个server
server = flask.Flask(__name__)


# 使用装饰器，将get_all_user函数变为一个接口 127.0.0.1:8085/api/v1/operation/zcmCustomer/startProcess
# 调用时直接访问该接口地址
@server.route('/api/v1/operation/zcmCustomer/startProcess', methods=['get', 'post'])
def get_all_user():
    mock_data = {"flag": bool('true'),
                 "statusCode": "20000", "statusDescription": "操作成功",
                 "data": {"pageNum": 1, "pageSize": 4, "size": 0, "startRow": 0, "endRow": 0, "total": 0, "pages": 0,
                          "list": [], "prePage": 0, "nextPage": 0, "isFirstPage": 'true', "isLastPage": 'false',
                          "hasPreviousPage": 'false', "hasNextPage": 'false', "navigatePages": 8, "navigatepageNums": [],
                          "navigateFirstPage": 0, "navigateLastPage": 0, "firstPage": 0, "lastPage": 0}}
    return mock_data


# 启动服务，debug=True 表示修改代码后自动重启
# 启动服务后接口才能正常访问，端口号为8085，默认地址为127.0.0.1


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=8085, debug=True)