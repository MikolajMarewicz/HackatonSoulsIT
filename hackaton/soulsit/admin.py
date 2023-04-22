from django.contrib import admin

from .models import Project

admin.site.register(Project)

from .models import Profile

# Register your models here.
admin.site.register(Profile)
