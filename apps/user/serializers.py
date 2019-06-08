from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator
from user.models import VerifyCode

User = get_user_model()

class EmailSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=50)
    def validate_email(self, email):
        if User.objects.filter(email=email).count():
            raise serializers.ValidationError("用户已经存在")
        return email

class UserRegSerializer(serializers.ModelSerializer):
    code = serializers.CharField(required=True, write_only=True, max_length=4, min_length=4, label="验证码",
                                 error_messages={
                                     "blank": "请输入验证码",
                                     "required": "请输入验证码",
                                     "max_length": "验证码格式错误",
                                     "min_length": "验证码格式错误"
                                 },
                                 help_text="验证码")
    username = serializers.CharField(label="用户名", help_text="用户名", required=True, allow_blank=False,
                                     validators=[UniqueValidator(queryset=User.objects.all(), message="用户已经存在")])

    password = serializers.CharField(
        style={'input_type': 'password'}, help_text="密码", label="密码", write_only=True,min_length=6
    )

    def validate_code(self, code):

        verify_records = VerifyCode.objects.filter(email=self.initial_data["email"]).order_by("-add_time")
        if verify_records:
            last_record = verify_records[0]
            print(last_record,code)
            print(last_record.add_time)
            if last_record.code != code:
                raise serializers.ValidationError("验证码错误")

        else:
            raise serializers.ValidationError("邮箱与验证邮箱不同")


    def validate(self, attrs):
        del attrs["code"]
        return attrs

    class Meta:
        model = User
        fields = ("username", "email","password","code")
