# Generated by Django 5.0.6 on 2024-07-25 04:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cso_app', '0040_cso_rankings_score'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cso_rankings',
            name='ranking_logo',
        ),
    ]
