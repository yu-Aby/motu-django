from rest_framework import serializers
from .models import UserCommment
from user.models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ("username",)

class UserCommmentSerializers(serializers.ModelSerializer):
    user = UserProfileSerializer()
    class Meta:
        model = UserCommment
        fields = ('user','tour','content','id','add_time')


