# Generated by Django 4.0.5 on 2022-06-16 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_employee_supervisor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='position',
            field=models.CharField(max_length=20),
        ),
    ]