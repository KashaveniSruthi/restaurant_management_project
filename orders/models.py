from django.db import models

# Create your models here.
class RestaurantInfo(models.Model):
    name=models.CharField(max_length=255)
    def__str__(self):
        return self.name
