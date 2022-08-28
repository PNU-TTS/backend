# Generated by Django 4.0.6 on 2022-08-23 05:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('certificate', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='buyer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='buyer_info', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='transaction',
            name='supplier',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='supplier_info', to=settings.AUTH_USER_MODEL),
        ),
    ]