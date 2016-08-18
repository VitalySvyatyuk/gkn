from django.db import models

class Order(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    total = models.FloatField()
    email = models.CharField(max_length=30)