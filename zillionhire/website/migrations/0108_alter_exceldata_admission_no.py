# Generated by Django 5.0.1 on 2024-02-22 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0107_rename_admission_number_exceldata_admission_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exceldata',
            name='admission_no',
            field=models.CharField(max_length=20),
        ),
    ]