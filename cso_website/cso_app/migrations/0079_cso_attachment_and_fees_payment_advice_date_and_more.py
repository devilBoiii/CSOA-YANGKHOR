# Generated by Django 5.0.6 on 2024-08-14 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cso_app', '0078_cso_attachment_and_fees_ref_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='cso_attachment_and_fees',
            name='payment_advice_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cso_attachment_and_fees',
            name='payment_advice_no',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
