# Generated by Django 4.2.10 on 2024-03-14 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_management', '0007_alter_blogpost_category_alter_blogpost_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='speciality',
            field=models.CharField(blank=True, choices=[('Dermatology', 'Dermatology'), ('General medicine', 'General medicine'), ('ENT', 'ENT'), ('Cardiology', 'Cardiology'), ('Gynaecology', 'Gynaecology')], max_length=100),
        ),
        migrations.AddField(
            model_name='doctor',
            name='name',
            field=models.CharField(default='10-10-2024', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='doctor',
            name='profilepic',
            field=models.ImageField(default='02-03-1999', upload_to='profile_pics/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='doctor',
            name='speciality',
            field=models.CharField(choices=[('Dermatology', 'Dermatology'), ('General medicine', 'General medicine'), ('ENT', 'ENT'), ('Cardiology', 'Cardiology'), ('Gynaecology', 'Gynaecology')], default='02/04/1999', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_patient',
            field=models.BooleanField(default=False),
        ),
    ]
