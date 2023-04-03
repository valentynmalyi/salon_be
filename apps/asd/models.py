from django.db import models


class Person(models.Model):
    name = models.TextField()
    asd = models.BooleanField(default=False)
