# Generated by Django 5.0.3 on 2024-03-15 08:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0133_addaptitude_jobb'),
    ]

    operations = [
        migrations.RenameField(
            model_name='addaptitude',
            old_name='jobb',
            new_name='job_id',
        ),
    ]
