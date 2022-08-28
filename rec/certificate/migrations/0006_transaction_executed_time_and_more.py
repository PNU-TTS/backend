# Generated by Django 4.0.1 on 2022-08-28 06:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificate', '0005_transaction_registered_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='executed_time',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='registered_time',
            field=models.DateField(default=datetime.datetime(2022, 8, 28, 15, 9, 43, 368039)),
        ),
    ]
