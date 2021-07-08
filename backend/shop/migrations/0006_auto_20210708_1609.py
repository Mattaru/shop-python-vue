# Generated by Django 3.2.5 on 2021-07-08 13:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0005_auto_20210708_1547'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='uuid',
        ),
        migrations.AddField(
            model_name='order',
            name='order_number',
            field=models.UUIDField(default=uuid.uuid4, unique=True, verbose_name='order number'),
        ),
        migrations.AddField(
            model_name='refund',
            name='accepted',
            field=models.BooleanField(default=False, verbose_name='accepted'),
        ),
        migrations.AddField(
            model_name='refund',
            name='order_number',
            field=models.UUIDField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='refund',
            name='reason',
            field=models.TextField(blank=True, verbose_name='reason'),
        ),
        migrations.AddField(
            model_name='refund',
            name='request_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='order date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='refund',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
    ]
