# Generated by Django 2.2.5 on 2019-10-29 12:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('conf', '0002_configuration_reseller'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configuration',
            name='reseller',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
    ]