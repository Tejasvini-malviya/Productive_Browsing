from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class RestrictedSite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

class TimeLimit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.URLField()
    time_limit = models.IntegerField(help_text="Time limit in minutes")
    created_at = models.DateTimeField(auto_now_add=True)

class UsageLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.URLField()
    time_spent = models.IntegerField(help_text="Time spent in seconds")
    visit_date = models.DateField(auto_now_add=True)
    active_time = models.IntegerField(help_text="Active time in seconds", default=0)
    idle_time = models.IntegerField(help_text="Idle time in seconds", default=0)
    