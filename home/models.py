from django.db import models

# Create your models here.
class RestaurantInfo(models.Model):
    name=model.CharField(max_length=255)
    description=models.textField(blank=True)
    image=models.ImageField(upload_to='restaurant_images/',blank=True)
    def __str__(self):
        return self.name