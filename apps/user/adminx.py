import xadmin
from xadmin import views
from .models import VerifyCode,UserProfile

class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = "墨途后台"
    site_footer = "motu"

class UserProfileAdmin():
    list_display = ['username','birthday','email','gender']

class VerifyCodeAdmin():
    list_display = ['code','email','add_time']

xadmin.site.register(VerifyCode, VerifyCodeAdmin)
# xadmin.site.unregister(UserProfile)
# xadmin.site.register(UserProfile, UserProfileAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)


