# Generated by Django 5.0.6 on 2024-08-08 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cso_app', '0061_financial_attachments_financial_class_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedBackForm',
            fields=[
                ('feedback_id', models.AutoField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('mobile_number', models.IntegerField(blank=True, null=True)),
                ('subject', models.CharField(blank=True, max_length=200, null=True)),
                ('message', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='financial_group',
            name='financial_group_status',
            field=models.CharField(blank=True, default='Active', max_length=200, null=True),
        ),
    ]
