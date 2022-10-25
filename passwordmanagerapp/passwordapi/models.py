from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Quicker(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    org_name = models.CharField(max_length=150)
    org_password = models.CharField(max_length=120)
    date_created = models.DateTimeField(auto_now_add=True)
    last_edited = models.DateTimeField(auto_now_add=True)