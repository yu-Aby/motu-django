from datetime import datetime

from django.db import models
from user.models import UserProfile
from place.models import Tours
# Create your models here.

class UserCommment(models.Model):
    user = models.ForeignKey(UserProfile,verbose_name="评论用户")
    tour = models.ForeignKey(Tours,verbose_name="评论景点")
    content = models.TextField(verbose_name="评论内容",default="")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        if self.user.name:
            return self.user.name
        else:
            return self.user.email
