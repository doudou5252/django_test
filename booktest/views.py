from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from booktest.models import BookInfo

# Create your views here.


def index(request):
    '''显示图书信息'''
    books = BookInfo.objects.all()
    # 使用模版
    return render(request, 'booktest/index.html', {'books': books})
    # return HttpResponse(books)

