# Generated by Django 5.0.6 on 2024-08-14 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cso_app', '0077_cso_attachment_and_fees_payment_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='cso_attachment_and_fees',
            name='ref_no',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
    ]
