# Generated by Django 4.2.10 on 2024-03-09 04:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_management', '0004_blogcategory_blogpost'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BlogPost',
        ),
    ]
