# Generated by Django 5.0.6 on 2024-08-30 09:35

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cso_app', '0091_page_contents_alter_notifications_notifications_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='page_contents',
            old_name='page',
            new_name='website_page',
        ),
        migrations.AlterField(
            model_name='notifications',
            name='notifications_id',
            field=models.UUIDField(default=uuid.UUID('88429e53-2f30-4205-bc89-c586bff2d991'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='page_contents',
            name='content_id',
            field=models.UUIDField(default=uuid.UUID('c1b70e58-ad6e-475f-8261-3ffe658f1fe9'), editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='post_publish',
            name='post_id',
            field=models.UUIDField(default=uuid.UUID('47b1c820-cad9-4300-b164-6baaa8a149de'), editable=False, unique=True),
        ),
    ]
