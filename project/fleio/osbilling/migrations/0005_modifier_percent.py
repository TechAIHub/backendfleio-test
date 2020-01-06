# Generated by Django 2.1.5 on 2019-02-05 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('osbilling', '0004_update_resource_attributes'),
    ]

    operations = [
        migrations.AddField(
            model_name='pricingrulemodifier',
            name='price_is_percent',
            field=models.BooleanField(default=False, help_text='Weather the price is a percent or an actual price'),
        ),
    ]