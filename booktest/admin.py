from django.contrib import admin
from booktest.models import BookInfo
from booktest.models import HeroInfo


# Register your models here.
# 注册模型类
admin.site.register(BookInfo)
admin.site.register(HeroInfo)

