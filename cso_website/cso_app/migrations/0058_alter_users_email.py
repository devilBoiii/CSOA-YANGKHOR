# Generated by Django 5.0.6 on 2024-08-02 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cso_app', '0057_users_groups_users_is_active_users_is_staff_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.EmailField(max_length=220),
        ),
    ]
