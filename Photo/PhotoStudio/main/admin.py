from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(addcategory)
admin.site.register(photo)
admin.site.register(userprofile)