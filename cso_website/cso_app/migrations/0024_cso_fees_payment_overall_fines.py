# Generated by Django 5.0.6 on 2024-07-11 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cso_app', '0023_remove_cso_fees_payment_payment_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='cso_fees_payment',
            name='overall_fines',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=15),
            preserve_default=False,
        ),
    ]
