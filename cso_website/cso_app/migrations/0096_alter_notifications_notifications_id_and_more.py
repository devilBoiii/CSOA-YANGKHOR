# Generated by Django 5.0.6 on 2024-09-19 11:41

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cso_app', '0095_alter_notifications_notifications_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notifications',
            name='notifications_id',
            field=models.UUIDField(default=uuid.UUID('835cc356-46b5-4450-8bf5-4087489df199'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='page_contents',
            name='content_id',
            field=models.UUIDField(default=uuid.UUID('39f56bdc-debc-4735-8bb3-b7c58c743a57'), editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='post_publish',
            name='post_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
