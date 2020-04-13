from django.db import models

# Create your models here.

class PizzaShop(models.Model):
    name = models.CharField(max_length=30, verbose_name="Pizza Hut")
    description = models.TextField(verbose_name="Description")
    rating = models.FloatField(verbose_name="Rating", default=0)
    url = models.URLField(verbose_name="internet address")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Пиццерия"
        verbose_name_plural = "Пиццерии"

class Pizza(models.Model):
    pizzaShop = models.ForeignKey(PizzaShop, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, verbose_name="Pizza name")
    short_description = models.CharField(max_length=30, verbose_name="Short description")
    price = models.IntegerField(default=0, verbose_name="price")
    photo = models.ImageField('Фото', upload_to='firsapp/photos', default='', blank=True)

    def __str__ (self):
        return self.name

    class Meta:
        verbose_name = "Пицца"
        verbose_name_plural = "Пиццы"
        ordering = ["name"]


class Order (models.Model):
    pizza = models.ForeignKey(Pizza, verbose_name="Пицца", on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Имя', max_length=30)
    phone = models.CharField(max_length=30, verbose_name='Телефон')
    date = models.DateTimeField(auto_now_add=True, verbose_name='дата')