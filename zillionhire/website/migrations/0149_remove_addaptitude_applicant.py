# Generated by Django 5.0.3 on 2024-03-18 04:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0148_addaptitude_applicant_addaptitude_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addaptitude',
            name='applicant',
        ),
    ]
