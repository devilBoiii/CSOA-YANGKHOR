# Generated by Django 5.0.6 on 2024-07-11 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cso_app', '0026_remove_cso_fees_payment_days_fine'),
    ]

    operations = [
        migrations.AddField(
            model_name='cso_fees_payment',
            name='cso_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
