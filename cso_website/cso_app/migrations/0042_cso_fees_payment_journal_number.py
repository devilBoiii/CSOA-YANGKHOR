# Generated by Django 5.0.6 on 2024-07-25 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cso_app', '0041_remove_cso_rankings_ranking_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='cso_fees_payment',
            name='journal_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
