from datetime import datetime

from django.db import models

# Create your models here.

class City(models.Model):
    name = models.CharField(max_length=300,verbose_name="城市名")
    code = models.CharField(max_length=300,verbose_name="城市名code")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    class Meta:
        verbose_name = '城市'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name



class Tours(models.Model):
    city = models.ForeignKey(City,verbose_name="所属城市")
    title = models.CharField(max_length=300,verbose_name="景点名")
    desc = models.CharField(max_length=300,verbose_name="描述")
    place = models.CharField(max_length=300,verbose_name="地址")
    img = models.CharField(max_length=300,verbose_name="图片")
    time = models.CharField(max_length=300,verbose_name="开放时间",null=True,blank=True)
    price = models.FloatField(verbose_name="门票价格",null=True,blank=True)
    detail_desc = models.TextField(verbose_name="详细描述",null=True,blank=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    class Meta:
        verbose_name = '景点'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title