import os
import sys
pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd+"../")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Travel.settings")

import django
django.setup()

from place.models import City

from db_tools.data.city import row_data

for city_detail in row_data:
    city = City()
    city.name = city_detail["name"]
    city.code = city_detail["code"]
    city.save()
