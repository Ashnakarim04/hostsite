# Generated by Django 5.0.1 on 2024-01-30 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0074_interdetails_classdetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentprofile',
            name='is_alumni',
            field=models.BooleanField(default=False),
        ),
    ]