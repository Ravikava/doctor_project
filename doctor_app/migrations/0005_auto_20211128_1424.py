# Generated by Django 3.2.9 on 2021-11-28 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor_app', '0004_faculty_student_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='master',
            name='Email',
            field=models.EmailField(default='', max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='master',
            name='Password',
            field=models.CharField(default='', max_length=12),
        ),
    ]
