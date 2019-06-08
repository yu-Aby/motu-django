from django_filters import rest_framework as filters
from .models import Tours

class ToursFilter(filters.FilterSet):
    title = filters.CharFilter(field_name='title',lookup_expr='icontains')
    city = filters.CharFilter(field_name='city__name',lookup_expr='icontains')
    id = filters.NumberFilter(field_name='id')
    class Meta:
        model = Tours
        fields = ['title', 'city','id']
