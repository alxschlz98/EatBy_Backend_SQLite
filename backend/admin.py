from django.contrib import admin
from .models import Grocery, Pantry, Trends

# Register your models here.

admin.site.register(Grocery)
admin.site.register(Pantry)
admin.site.register(Trends)
