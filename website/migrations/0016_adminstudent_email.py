# Generated by Django 4.2.5 on 2023-09-27 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0015_jobs_is_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='adminstudent',
            name='email',
            field=models.EmailField(max_length=255, null=True),
        ),
    ]