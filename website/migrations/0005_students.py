# Generated by Django 4.2.4 on 2023-09-14 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_jobs_is_active_alter_companyprofile_city_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('course', models.CharField(choices=[('B.Tech', 'B.Tech'), ('MCA', 'MCA')], max_length=50)),
                ('department', models.CharField(choices=[('ECE', 'ECE'), ('CSE', 'CSE'), ('Integrated MCA', 'Integrated MCA'), ('Regular MCA', 'Regular MCA')], max_length=100)),
                ('semester', models.CharField(choices=[('Semester 1', 'Semester 1'), ('Semester 2', 'Semester 2'), ('Semester 3', 'Semester 3'), ('Semester 4', 'Semester 4'), ('Semester 5', 'Semester 5'), ('Semester 6', 'Semester 6'), ('Semester 7', 'Semester 7'), ('Semester 8', 'Semester 8'), ('Semester 9', 'Semester 9'), ('Semester 10', 'Semester 10')], max_length=100)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]