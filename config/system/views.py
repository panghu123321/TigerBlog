import json
import os
from django.shortcuts import render, redirect
from django.http.response import JsonResponse
from TigerBlog.settings import VERSION, INIT_STATUS, BASE_DIR
from config.system.models import System
from django.contrib.auth.models import User

init = INIT_STATUS


def install(request):
    global init
    if request.method == 'GET':
        # 项目初始化后访问，重定向到首页
        if init:
            return redirect('/')
        data = {
            'version': VERSION
        }
        return render(request=request, template_name='page/init/init.html', context=data)
    elif request.method == 'POST':
        data = json.loads(request.body)
        username = data['blog_user']
        password = data['blog_password']
        email = data['blog_email']
        hostname = [f'{data["blog_domain"]}']
        title = data['blog_title']
        if hostname == 'localhost' or hostname == '127.0.0.1':
            hostname = []
        # 保存系统配置
        try:
            system = System.objects.get(id=1)
            system.init = True,
            system.title = title,
            system.hostname = hostname,
            system.debug = False
            system.save()
        except System.DoesNotExist:
            System.objects.create(
                init=True,
                title=title,
                hostname=hostname,
                debug=False
            ).save()
        try:
            user = User.objects.get(id=1)
            user.username = username
            user.password = password
            user.email = email
            user.save()
        except User.DoesNotExist:
            User.objects.create(
                username=username,
                password=password,
                email=email,
            ).save()
        config = json.loads(open(os.path.join(BASE_DIR, 'config.json'), 'r').read())
        config['ALLOWED_HOSTS'] = hostname
        config['DEBUG'] = True
        config['INIT_STATUS'] = True
        config['TITLE'] = title
        open(os.path.join(BASE_DIR, 'config.json'), 'w').write(json.dumps(config))
        init = True
        return JsonResponse({'result': False, 'status': 200, 'message': '安装成功！'})

    else:
        return JsonResponse({'result': False, 'status': 201, 'message': '请使用GET/POST方式请求！'})
