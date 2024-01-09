#!/user/bin/env python3
# -*- coding: utf-8 -*-
from rest_framework.response import Response


# class BaseResponse(object):
#     def __init__(self):
#         self.code = 200
#         self.data = None
#         self.error = None
#
#     @property
#     def dict(self):
#         return self.__dict__

class BaseResponse(Response):
    def __init__(self, data=None, status=None, msg=None, template_name=None, headers=None,
                 exception=False, content_type=None):
        # 自定义返回格式
        formatted_data = {
            'status': status if status is not None else self.status_code,
            'data': data,
            'msg': msg,
        }
        super().__init__(formatted_data, status=status, template_name=template_name,
                         headers=headers, exception=exception, content_type=content_type)
