# Generated by Django 2.2.2 on 2019-07-01 09:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('openstack', '0022_openstackregion_disable_for_enduser'),
    ]

    operations = [
        migrations.AddField(
            model_name='volumebackup',
            name='region',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='openstack.OpenstackRegion'),
        ),
    ]