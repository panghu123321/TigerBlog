import json
import os

from django.shortcuts import redirect
from django.urls import reverse

from TigerBlog.settings import BASE_DIR


class InitializationMiddleware:
    """
    初始化中间件，访问时判断项目是否初始化，未初始化时将重定向到 /install/ 页面
    """

    def __init__(self, get_response):
        self.get_response = get_response
        self.init = None

    def __call__(self, request):
        """
        在每个请求进入时，它会检查 c 字段
        """
        # 从配置文件中读取是否初始化项目
        if not self.init:
            self.init = json.loads(open(os.path.join(BASE_DIR, 'config.json'), 'r').read())['INIT_STATUS']
        # 当初始化状态为 False 时，所有链接访问都重定向到 /install/
        if not self.init and request.path != reverse('install'):
            return redirect('install')
        # 初始化状态为 True 时，所有链接访问正常
        response = self.get_response(request)
        return response
