# Generated by Django 4.0.1 on 2022-08-28 06:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificate', '0004_alter_transaction_buyer'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='registered_time',
            field=models.DateField(default=datetime.datetime(2022, 8, 28, 15, 8, 32, 344292)),
        ),
    ]
