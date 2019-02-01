from django.db import models

# Create your models here.
class BookInfo(models.Model):
    btitle = models.CharField(max_length=30)
    bpub_date = models.DateField()
    bread = models.IntegerField(default=0)
    bcomment = models.IntegerField(default=0)
    isDelete = models.BooleanField(default=False)
    def __str__(self):
        # 返回英雄名
        return self.btitle

# 多类
class HeroInfo(models.Model):
    hname = models.CharField(max_length=30)
    hgender = models.BooleanField(default=False)
    hcomment = models.CharField(max_length=200)
    hbook = models.ForeignKey('BookInfo', on_delete=models.CASCADE)
    isDelete = models.BooleanField(default=False)
    def __str__(self):
        # 返回英雄名
        return self.hname
