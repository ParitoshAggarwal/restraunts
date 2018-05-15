from django.db import models
from django.conf import settings
# Create your models here.

User = settings.AUTH_USER_MODEL


class restlist(models.Model):
    owner = models.ForeignKey(User)
    name = models.CharField(max_length=120)
    location = models.CharField(max_length=120, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
