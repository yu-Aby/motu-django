import xadmin
from .models import City,Tours

class CityAdmin:
    list_display = ["name","code","add_time"]
    search_fields = ["name",]
    list_filter = ["name","code"]

class TourAdmin:
    list_display = ["city","title","place","price","add_time"]
    search_fields = ["title","city__name"]
    list_filter = ["city",]


xadmin.site.register(City,CityAdmin)
xadmin.site.register(Tours,TourAdmin)