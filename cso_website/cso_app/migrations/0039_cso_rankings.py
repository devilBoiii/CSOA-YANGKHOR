# Generated by Django 5.0.6 on 2024-07-24 06:50

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cso_app', '0038_alter_cso_fees_payment_annual_general_report'),
    ]

    operations = [
        migrations.CreateModel(
            name='cso_rankings',
            fields=[
                ('cso_rankings_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('cso_name', models.CharField(blank=True, max_length=200, null=True)),
                ('rank', models.IntegerField(blank=True, null=True)),
                ('ranking_logo', models.FileField(blank=True, null=True, upload_to='cso_rank/')),
                ('cso_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cso_app.cso_lists')),
            ],
        ),
    ]
