from django.db import models
from taggit.managers import TaggableManager

class Property(models.Model):
    description = models.TextField()
    # pictures = models.ImageField(null=True)
    city = models.CharField(max_length = 30)
    surburb = models.CharField(max_length=30)
    street_address = models.CharField(max_length=30)
    max_guest = models.IntegerField()
    guest_price_night = models.DecimalField(max_digits=10 ,decimal_places=2)
    extra_guest_price_night = models.DecimalField(max_digits=10 ,decimal_places=2)
    tags = TaggableManager()

class PropertyImage(models.Model):
    property_image = models.ForeignKey(Property, default=None, on_delete=models.CASCADE)
    pictures = models.ImageField(upload_to='pictures/')