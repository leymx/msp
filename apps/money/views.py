# -*- coding:utf-8 -*-

from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'mspbase.html')



# ------ 理财信息记录的操作接口 ------
def save(request):
    pass

def query(request):
    pass

def delete(request):
    pass


