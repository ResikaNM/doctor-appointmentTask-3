# Generated by Django 4.2.10 on 2024-03-06 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_management', '0002_alter_customuser_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='pincode',
            field=models.IntegerField(default=0),
        ),
    ]