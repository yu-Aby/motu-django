import xadmin
from .models import UserCommment

class UserCommmentAdmin:
    list_display = ['user','tour']
    search_fields = ['user__name','tour__title']

xadmin.site.register(UserCommment,UserCommmentAdmin)