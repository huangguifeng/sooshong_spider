# -*- coding=utf-8 -*-

import random
import base64
from myproxy import PROXY
from settings import USER_AGENTS

class RandomUserAgentMiddleware(object):

    def process_request(self,request,spider):
        user_agent = random.choice(USER_AGENTS)
        request.headers.setdefault('User-Agent', user_agent)


# class ProxyMiddleware(object):
#
#     def process_request(self,request,spider):
#         # # 　免认证代理
#         # random_proxy = random.choice(PROXY)
#         # request.meta['proxy']='https://'+'113.108.130.210:9000'
#
#
#         # # 需要认证代理写法
#         #
#         #
#         proxy = "116.62.128.50:16816"
#         request.meta["proxy"] = "http://" + proxy
#         proxy_user_passwd = "mr_mao_hacker:sffqry9r"
#         base64_user_passwd = base64.b64encode(proxy_user_passwd)
#         request.headers["Proxy-Authorization"] = "Basic " + base64_user_passwd
#         #
class CodeMiddleware(object):
    def process_response(self, request, response, spider):
        res = response.replace(body = response.body.decode(response.encoding).encode("utf-8"), encoding = "utf-8")
        return res

