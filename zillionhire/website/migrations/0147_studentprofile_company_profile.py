# Generated by Django 5.0.3 on 2024-03-17 19:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0146_questionn_marks'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentprofile',
            name='company_profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='website.companyprofile'),
        ),
    ]
