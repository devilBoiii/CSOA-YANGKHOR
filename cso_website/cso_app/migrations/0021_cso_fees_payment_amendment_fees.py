# Generated by Django 5.0.6 on 2024-07-11 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cso_app', '0020_rename_amendment_fees_cso_fees_payment_fees_payment_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cso_fees_payment',
            name='amendment_fees',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
