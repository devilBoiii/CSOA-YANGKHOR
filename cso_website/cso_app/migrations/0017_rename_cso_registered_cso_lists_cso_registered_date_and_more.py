# Generated by Django 5.0.6 on 2024-07-04 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cso_app', '0016_cso_lists_cso_acronym_cso_lists_registration_no_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cso_lists',
            old_name='cso_registered',
            new_name='cso_registered_date',
        ),
        migrations.RenameField(
            model_name='cso_lists',
            old_name='cso_validy',
            new_name='cso_validy_date',
        ),
        migrations.RemoveField(
            model_name='cso_lists',
            name='registration_date',
        ),
    ]
