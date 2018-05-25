from django.shortcuts import render
from django.http import HttpResponse
import requests
from app.models import Actionlog
from app.models import Today
from django.forms.models import model_to_dict
from django.core import serializers
import datetime
import json
# coding:utf-8
# Create your views here.
def index(request):
    string = "我在自强学堂学习Django，用它来建网站"
    return render(request, 'home.html',{'string': string})
    # return HttpResponse(u"欢迎光临 自强学堂!")

def today(request):
    time=datetime.datetime.now().strftime('%Y-%m-%d')
    try:
        data = Today.objects.get(date=time)
        return render(request, 'today.html', {'arrData': eval(data.json)})
    except Today.DoesNotExist:
        url = 'https://xcx.77masion.top/masion77/index/gethistorytoday'
        r = requests.post(url, data={})
        jsonData=r.json()
        # 保存数据
        Today.objects.create(date=time, json=jsonData)
        return render(request, 'today.html', {'arrData': jsonData})

def db(request):
    try:
        twz = Actionlog.objects.get(id=1)
    except Actionlog.DoesNotExist:
        twz = {}
    u_dict = model_to_dict(twz)
    # if(twz):
    #     u_dict = model_to_dict(twz)
    # else:
    #     u_dict = {}
    # data = serializers.serialize("json", twz)
    # twz.dist = "tuweizhong@163.com"
    # res=twz.save()
    # return HttpResponse(json.dumps(twz,ensure_ascii=False, encoding='UTF-8'))
    return HttpResponse(json.dumps(u_dict))