# Generated by Django 2.1.5 on 2019-02-05 12:31

from django.db import migrations
from django.db import transaction
from django.db import utils


def add_swift_resources(apps, schema_editor):
    """Add osbilling resources with attributes and metrics"""
    resource = apps.get_model("osbilling", "BillingResource")

    swift_metrics = {
        "metrics": [
            {
                "rescale_to": "g",
                "name": "storage.objects.incoming.bytes",
                "aggregation": "sum",
                "reaggregation": "sum",
                "granularity": 300,
                "unit": "b"
            },
            {
                "rescale_to": "g",
                "name": "storage.objects.outgoing.bytes",
                "aggregation": "sum",
                "reaggregation": "sum",
                "granularity": 300,
                "unit": "b"
            },
            {
                "name": "storage.api.requests",
                "aggregation": "sum",
                "reaggregation": "sum",
                "granularity": 300
            },
            {
                "name": "storage.objects",
                "aggregation": "mean",
                "reaggregation": "mean",
                "granularity": 300
            },
            {
                "name": "storage.objects.containers",
                "aggregation": "mean",
                "reaggregation": "mean",
                "granularity": 300
            },
            {
                "rescale_to": "g",
                "name": "storage.objects.size",
                "aggregation": "mean",
                "reaggregation": "mean",
                "granularity": 300,
                "unit": "b"
            }
        ]
    }

    network_metrics = {
        "metrics": [
            {
                "rescale_to": "g",
                "name": "bandwidth",
                "aggregation": "sum",
                "reaggregation": "sum",
                "granularity": 300,
                "unit": "b"
            },
            {
                "name": "ip.floating",
                "aggregation": "mean",
                "reaggregation": "mean",
                "granularity": 300
            }
        ]
    }

    try:
        with transaction.atomic():
            resource.objects.filter(name='network').update(definition=network_metrics)
            resource.objects.create(name='swift_account',
                                    type='metric',
                                    display_name='Object storage',
                                    definition=swift_metrics)
    except utils.IntegrityError:
        pass


class Migration(migrations.Migration):
    dependencies = [
        ('osbilling', '0006_update_condition_and_modifier_choices_for_pricing_rule'),
    ]

    operations = [
        migrations.RunPython(add_swift_resources),
    ]