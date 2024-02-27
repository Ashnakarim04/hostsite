# Generated by Django 5.0.1 on 2024-02-27 09:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0112_aptitudetest'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.TextField()),
                ('answer_type', models.CharField(choices=[('radio', 'Radio Button'), ('checkbox', 'Checkbox'), ('text', 'Text Box')], max_length=10)),
                ('options', models.JSONField(blank=True, null=True)),
                ('answer', models.TextField(blank=True, null=True)),
                ('aptitude_test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.aptitudetest')),
            ],
        ),
    ]
