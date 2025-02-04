# Generated by Django 5.0.6 on 2024-07-04 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cso_app', '0015_remove_cso_lists_registration_fee_due_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cso_lists',
            name='cso_acronym',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='cso_lists',
            name='registration_no',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='cso_lists',
            name='reporting_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cso_lists',
            name='thematic_area',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
