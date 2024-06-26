# Generated by Django 5.0.3 on 2024-03-30 08:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0174_aptresult'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResultAptitude',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_marks', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.companyprofile')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.studentprofile')),
            ],
        ),
        migrations.DeleteModel(
            name='AptResult',
        ),
    ]
