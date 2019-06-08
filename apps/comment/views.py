from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserCommmentSerializers
from rest_framework import viewsets, status
from .models import UserCommment
from user.models import UserProfile
from place.models import Tours
from django_filters import rest_framework as filters
# Create your views here.

class UserCommmentView(viewsets.ModelViewSet):
    serializer_class = UserCommmentSerializers
    queryset = UserCommment.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('tour',)

    def create(self, request, *args, **kwargs):
        data=request.data
        # print(UserCommment)
        # print(data)
        user = UserProfile.objects.get(username=data['username'])
        tour = Tours.objects.get(id=data['tour'])
        UserCommment.objects.create(user=user,tour=tour,content=data['content'])
        return Response(status=status.HTTP_201_CREATED)
