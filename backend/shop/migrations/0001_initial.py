# Generated by Django 3.2.5 on 2021-07-07 10:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, verbose_name='name')),
                ('slug', models.CharField(blank=True, max_length=255, null=True, unique=True, verbose_name='slug')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, verbose_name='name')),
                ('slug', models.CharField(blank=True, max_length=255, null=True, unique=True, verbose_name='slug')),
                ('quantity', models.IntegerField(verbose_name='quantity')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='price')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='shop.category', verbose_name='category')),
            ],
        ),
    ]