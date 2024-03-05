# Generated by Django 5.0.1 on 2024-03-05 04:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0120_alumnievent'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True, verbose_name='status')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('date', models.DateField()),
                ('image', models.ImageField(upload_to='event_images/')),
                ('event_type', models.CharField(choices=[('offline', 'Offline'), ('online', 'Online')], max_length=10)),
                ('link', models.URLField()),
                ('company', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='website.companyprofile')),
            ],
        ),
    ]
