from uuid import uuid4
from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4
# Create your models here.
class CrudData(models.Model):
    id = models.UUIDField(primary_key=True,unique=True,default=uuid4)
    name = models.CharField(max_length=500)
    age = models.IntegerField(default=0)
    def __str__(self):
        return self.name

