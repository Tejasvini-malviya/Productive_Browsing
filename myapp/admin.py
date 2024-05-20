# admin.py

from django.contrib import admin
from .models import RestrictedSite, TimeLimit, UsageLog

# Register your models here.
admin.site.register(RestrictedSite)
admin.site.register(TimeLimit)
admin.site.register(UsageLog)
