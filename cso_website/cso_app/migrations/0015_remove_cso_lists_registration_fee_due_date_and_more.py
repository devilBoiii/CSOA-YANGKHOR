# Generated by Django 5.0.6 on 2024-07-04 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cso_app', '0014_cso_lists_remove_cso_fees_payment_fcso_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cso_lists',
            name='registration_fee_due_date',
        ),
        migrations.AddField(
            model_name='cso_lists',
            name='application_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cso_lists',
            name='registration_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
