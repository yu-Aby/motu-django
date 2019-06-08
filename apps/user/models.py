from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser

class UserProfile(AbstractUser):

    name = models.CharField(max_length=30,null=True,blank=True,verbose_name="姓名")
    birthday = models.DateField(null=True,blank=True,verbose_name="出生年月")
    mobile = models.CharField(max_length=11,verbose_name="电话",null=True,blank=True)
    gender = models.CharField(max_length=6,choices=(("male",u"男"),("female","女")),default="male",verbose_name="性别")
    email = models.CharField(max_length=100,null=True,blank=True,verbose_name="邮箱")

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户'

    def __str__(self):
        return self.username

class VerifyCode(models.Model):
    code = models.CharField(max_length=10,verbose_name="验证码")
    email = models.CharField(null=True,max_length=20,verbose_name="邮箱")

    add_time = models.DateTimeField(default=datetime.now,verbose_name="添加时间")

    class Meta:
        verbose_name = '邮箱验证码'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code


