# Generated by Django 5.0.3 on 2024-03-23 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0168_resumebuilder_address_resumebuilder_career_objective_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='resumebuilder',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='resume_images/'),
        ),
    ]