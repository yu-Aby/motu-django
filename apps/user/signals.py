from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

User=get_user_model()
#通过信号接收修改用户密码，加密
@receiver(post_save, sender=User)
def create_user(sender, instance=None, created=False, **kwargs):
#create判断是否是新建
    if created:
        if sender.is_superuser:
            return
        password=instance.password
        instance.set_password(password)
        instance.save()