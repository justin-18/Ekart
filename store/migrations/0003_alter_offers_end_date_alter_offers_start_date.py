# Generated by Django 5.0.3 on 2024-05-24 05:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_offers_end_date_alter_offers_start_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offers',
            name='end_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='offers',
            name='start_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
