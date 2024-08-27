# Generated by Django 5.0.6 on 2024-07-04 05:00

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cso_app', '0009_rename_mbo_list_mbo_lists'),
    ]

    operations = [
        migrations.AddField(
            model_name='fcso_lists',
            name='amendment_fee_due_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='fcso_lists',
            name='late_renewal_fee_due_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='fcso_lists',
            name='registration_fee_due_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='fcso_lists',
            name='renewal_fee_due_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mbo_lists',
            name='amendment_fee_due_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mbo_lists',
            name='late_renewal_fee_due_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mbo_lists',
            name='registration_fee_due_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mbo_lists',
            name='renewal_fee_due_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pbo_lists',
            name='amendment_fee_due_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pbo_lists',
            name='late_renewal_fee_due_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pbo_lists',
            name='registration_fee_due_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pbo_lists',
            name='renewal_fee_due_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='cso_fees_payment',
            fields=[
                ('payment_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('renewal_fees', models.CharField(blank=True, max_length=100, null=True)),
                ('amendment_fees', models.CharField(blank=True, max_length=100, null=True)),
                ('registration_fees', models.CharField(blank=True, max_length=100, null=True)),
                ('late_renewal_fees', models.CharField(blank=True, max_length=100, null=True)),
                ('payment_type', models.CharField(blank=True, max_length=150, null=True)),
                ('amount_paid', models.CharField(blank=True, max_length=150, null=True)),
                ('payment_screenshot', models.ImageField(blank=True, max_length=150, upload_to='images/')),
                ('payment_date', models.DateTimeField(auto_now_add=True)),
                ('fcso_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cso_app.fcso_lists')),
                ('mbo_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cso_app.mbo_lists')),
                ('pbo_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cso_app.pbo_lists')),
            ],
        ),
    ]
