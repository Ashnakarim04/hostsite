# Generated by Django 5.0.3 on 2024-03-17 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0145_remove_questionn_user_questionn_company_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionn',
            name='marks',
            field=models.DecimalField(decimal_places=2, default=1.0, max_digits=5),
        ),
    ]
