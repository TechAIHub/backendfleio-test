# Generated by Django 2.1.7 on 2019-03-07 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0008_order_domain'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='domain_name',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]