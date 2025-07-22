from django.db import models
from django.contrib.auth.models import User


class Category(models.Model ):
    title = models.CharField(max_length=223 )

    def __str__(self):
        return self.title


class Car(models.Model ):
    objects = None
    DoesNotExist = None
    title = models.CharField(max_length=323 )
    model = models.CharField(max_length=323 )
    category = models.ForeignKey(Category, on_delete=models.PROTECT, blank=True, null=True)
    year = models.PositiveSmallIntegerField()
    image = models.ImageField(upload_to='media/car_images' )
    price = models.DecimalField(decimal_places=2, max_digits=12)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return self.title
