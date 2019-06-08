from rest_framework import serializers


from .models import Tours,City



class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class TourSerializer(serializers.ModelSerializer):
    city = CitySerializer()
    class Meta:
        model = Tours
        fields = '__all__'