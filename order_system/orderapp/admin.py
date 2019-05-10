from django.contrib import admin
from .models import User, Order_from, Suggest, Restaurant, City

# Register your models here.
admin.site.register(User)
admin.site.register(Order_from)
admin.site.register(Suggest)
admin.site.register(Restaurant)
admin.site.register(City)
