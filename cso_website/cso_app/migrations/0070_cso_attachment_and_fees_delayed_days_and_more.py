# Generated by Django 5.0.6 on 2024-08-13 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cso_app', '0069_alter_cso_attachment_and_fees_cso_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='cso_attachment_and_fees',
            name='delayed_days',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cso_attachment_and_fees',
            name='late_report_fees',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
