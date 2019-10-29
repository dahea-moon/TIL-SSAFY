# Generated by Django 2.2.6 on 2019-10-22 00:54

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='fans',
            field=models.ManyToManyField(related_name='stars', to=settings.AUTH_USER_MODEL),
        ),
    ]
