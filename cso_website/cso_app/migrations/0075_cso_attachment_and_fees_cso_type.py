# Generated by Django 5.0.6 on 2024-08-13 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cso_app', '0074_alter_cso_attachment_and_fees_annual_general_report'),
    ]

    operations = [
        migrations.AddField(
            model_name='cso_attachment_and_fees',
            name='cso_type',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
