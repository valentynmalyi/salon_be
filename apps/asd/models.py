import django
from django.db import models

django.setup()


class Person(models.Model):
    name = models.TextField()
    asd = models.BooleanField(default=False)
