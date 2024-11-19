from django.contrib import admin
from .models import movie_info,CensorInfo
# Register your models here.
admin.site.register(movie_info)
admin.site.register(CensorInfo)