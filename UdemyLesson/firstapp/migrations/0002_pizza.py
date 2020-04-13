# Generated by Django 3.0.5 on 2020-04-13 05:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Pizza name')),
                ('short_description', models.CharField(max_length=30, verbose_name='Short description')),
                ('price', models.IntegerField(default=0, verbose_name='price')),
                ('pizzaShop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstapp.PizzaShop')),
            ],
        ),
    ]
