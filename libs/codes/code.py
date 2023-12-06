#!/user/bin/env python3
# -*- coding: utf-8 -*-

# Python状态码字典
status_codes = {
    200: "OK",
    201: "Created",
    204: "No Content",
    400: "Bad Request",
    401: "Unauthorized",
    403: "Forbidden",
    404: "Not Found",
    405: "Method Not Allowed",
    500: "Internal Server Error",
    502: "Bad Gateway",
    503: "Service Unavailable",
    504: "Gateway Timeout"
}

# 定义状态码的变量
HTTP_OK = 200
HTTP_CREATED = 201
HTTP_NO_CONTENT = 204
HTTP_BAD_REQUEST = 400
HTTP_UNAUTHORIZED = 401
HTTP_FORBIDDEN = 403
HTTP_NOT_FOUND = 404
HTTP_METHOD_NOT_ALLOWED = 405
HTTP_INTERNAL_SERVER_ERROR = 500
HTTP_BAD_GATEWAY = 502
HTTP_SERVICE_UNAVAILABLE = 503
HTTP_GATEWAY_TIMEOUT = 504


# 查询错误含义的函数
def get_error_description(status_code):
    """
    获取错误码的描述性注释

    Args:
        status_code (int): HTTP状态码

    Returns:
        str: 错误码的描述性注释，如果未找到则返回默认消息
    """
    return status_codes.get(status_code, "Unknown Status Code")
