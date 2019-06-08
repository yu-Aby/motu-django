"""Travel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.views.static import serve
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token
from Travel.settings import MEDIA_ROOT
from rest_framework.authtoken import views


import xadmin
from place.views import ToursView, CityView
from user.views import EmailCodeViewset, UserViewset
from comment.views import UserCommmentView

router = DefaultRouter()
router.register(r'codes', EmailCodeViewset, base_name="codes")
router.register(r'users', UserViewset, base_name="users")
router.register(r'tours', ToursView, base_name="tour")
router.register(r'citys', CityView, base_name="citys")
router.register(r'comment', UserCommmentView, base_name="comment")


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    url(r'^api-token-auth/', views.obtain_auth_token),
    # jwt
    url(r'^login/', obtain_jwt_token),
]
