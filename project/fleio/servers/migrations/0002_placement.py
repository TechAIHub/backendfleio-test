# Generated by Django 2.1.2 on 2018-12-06 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='servergroup',
            name='placement',
            field=models.PositiveIntegerField(choices=[(1, 'In order'), (2, 'Least full')], default=1, help_text='How accounts are created on servers in this group'),
        ),
    ]