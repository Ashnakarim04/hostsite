# Generated by Django 5.0.1 on 2024-01-31 08:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0080_ccontent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ccontent',
            name='status',
        ),
        migrations.AddField(
            model_name='ccontent',
            name='udate',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='ccontent',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]