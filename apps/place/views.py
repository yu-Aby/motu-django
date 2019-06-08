import django_filters
from django.shortcuts import render
from django_filters import rest_framework as filters
from rest_framework import viewsets, generics

from place.filter import ToursFilter
from .serializers import TourSerializer,CitySerializer
from .models import Tours,City
from rest_framework.pagination import PageNumberPagination
# Create your views here.

class TourPagination(PageNumberPagination):
    page_size = 15
    page_size_query_param = 'page_size'
    max_page_size = 100

class ToursView(viewsets.ModelViewSet,generics.ListAPIView):

    queryset = Tours.objects.all().order_by('id')
    serializer_class = TourSerializer
    pagination_class = TourPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ToursFilter
    # filterset_fields = ('city', 'title')

class CityView(viewsets.ModelViewSet):

    queryset = City.objects.all()
    serializer_class = CitySerializer

