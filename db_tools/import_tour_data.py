import os
import sys
pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd+"../")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Travel.settings")

import django
django.setup()

from place.models import Tours,City

from db_tools.data.tour import row_data

for tour_detail in row_data:
    tour = Tours()
    tour.title = tour_detail["title"]
    tour.desc = tour_detail["desc"]
    tour.img = tour_detail["img"]
    if tour_detail["price"] != '':
        tour.price = (float(int(tour_detail["price"])))
    tour.place = tour_detail["place"]
    tour.time = tour_detail["time"]
    tour.detail_desc = tour_detail["detail_desc"]
    city_name = tour_detail["city"]
    city = City.objects.filter(name=city_name)
    if city:
        tour.city = city[0]
    tour.save()