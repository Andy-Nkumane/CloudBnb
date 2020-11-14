from django.contrib import admin
from . import models

# Register your models here.

class PropertyImageAdmin(admin.StackedInline):
    model = models.PropertyImage

@admin.register(models.Property)
class PropertyAdmin(admin.ModelAdmin):
    inlines = [PropertyImageAdmin]

    class Meta:
        model = models.Property
