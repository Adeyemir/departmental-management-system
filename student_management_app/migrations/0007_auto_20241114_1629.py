# Generated by Django 3.0.7 on 2024-11-14 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0006_students_matric_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='matric_number',
            field=models.CharField(default='000000000', max_length=9),
        ),
    ]