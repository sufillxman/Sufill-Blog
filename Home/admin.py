from django.contrib import admin #type:ignore
from .models import BlogModel #type:ignore
# Register your models here.

admin.site.register(BlogModel)

