from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(default=18)
    title = models.CharField(max_length=50)
    hometown = models.CharField(max_length=50, blank=True, null=True)

