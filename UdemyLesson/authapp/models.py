from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class PizzaShop(models.Model):
    name = models.CharField(max_length=30)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='pizzashop')
    logo = models.ImageField(upload_to='pizzashop_logo', blank=False)

    def __str__(self):
        return self.name

