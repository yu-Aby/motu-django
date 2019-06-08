from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render
from random import choice
from django.core.mail import EmailMultiAlternatives
from rest_framework import status, mixins
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.mixins import CreateModelMixin
from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler

from user.models import VerifyCode
from .serializers import EmailSerializer, UserRegSerializer, User




class CustomBackend(ModelBackend):
    """
    自定义用户验证
    """
    def authenticate(self, username=None, password=None, **kwargs):
        # try:
        #     user = User.objects.get(Q(username=username)|Q(email=username))
        #     if user.check_password(password):
        #         return user
        # except Exception as e:
        #     return None
        try:
            user_error = {}
            user = User.objects.get(Q(username=username) | Q(email=username))
            if user :
                if user.check_password(password):
                    return user
                else :
                    user_error["password"] = '密码错误'
            else:
                user_error["user"] = '没有该用户'
            if user_error :
                return user
            else:
                return JsonResponse(user_error, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return None

class EmailCodeViewset(CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = EmailSerializer
    def generate_code(self):
        """
        生成四位数字的验证码
        :return:
        """
        seeds = "1234567890"
        random_str = []
        for i in range(4):
            random_str.append(choice(seeds))

        return "".join(random_str)
    # 发送邮件
    def send_email(self,email,code):

        subject, from_email, to = '来自墨途的验证码邮件', 'ngyfanyumo@163.com', email
        text_content = '您好，欢迎您注册墨途，本次注册的验证为' + code
        html_content = '<p>您好，欢迎您注册墨途，本次注册的验证码为 {} </p>'.format(code)
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data["email"]
        code = self.generate_code()
        self.send_email(email,code)
        code_record = VerifyCode(code=code, email=email)
        code_record.save()
        return Response({
            "email": email
        }, status=status.HTTP_201_CREATED)

class UserViewset(CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    用户
    """
    serializer_class = UserRegSerializer
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)

        re_dict = serializer.data
        payload = jwt_payload_handler(user)
        re_dict["token"] = jwt_encode_handler(payload)
        re_dict["name"] = user.name if user.name else user.username
        re_dict["id"] = user.id

        headers = self.get_success_headers(serializer.data)
        return Response(re_dict, status=status.HTTP_201_CREATED, headers=headers)

    def get_object(self):
        return self.request.user

    def perform_create(self, serializer):
        return serializer.save()

