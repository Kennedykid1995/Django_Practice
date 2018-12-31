from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User

# Create your models here.
class Listing(models.Model):
    id = models.UUIDFeild(primary_key = True, default = uuid4, editable=False)
    title = models.CharField(max_length = 120)
    description = models.TextFeild(blank = True)
    price = models.CharField(max_length = 50)