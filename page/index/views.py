from django.shortcuts import render, redirect, HttpResponse
from django.http.response import JsonResponse


def index(request):
    if request.method == "GET":
        return HttpResponse("ok")
    else:
        return JsonResponse({"result": False, "status": 201, "message": "请使用GET方式请求！"})
