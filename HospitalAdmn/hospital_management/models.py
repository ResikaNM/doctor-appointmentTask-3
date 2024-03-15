from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
# Create your models here.
class customUser(AbstractUser):
    profile_pic=models.ImageField(upload_to='profile_pics/',blank=True)
    is_patient=models.BooleanField(default=False)
    is_doctor=models.BooleanField(default=False)
    address_line1=models.CharField(max_length=250)
    city=models.CharField(max_length=250)
    state=models.CharField(max_length=250)
    pincode=models.IntegerField(default=0)
    SPECIALITY_CHOICES = [
        ('Dermatology', 'Dermatology'),
        ('General medicine', 'General medicine'),
        ('ENT', 'ENT'),
        ('Cardiology', 'Cardiology'),
        ('Gynaecology', 'Gynaecology'),
    ]
    speciality = models.CharField(max_length=100, choices=SPECIALITY_CHOICES, blank=True)


customUser._meta.get_field('groups').remote_field.related_name = 'custom_user_groups'
customUser._meta.get_field('user_permissions').remote_field.related_name = 'custom_user_permissions'

class Patient(models.Model):
    user=models.OneToOneField(customUser,on_delete=models.CASCADE)


# class Doctor(models.Model):
#     user=models.OneToOneField(customUser,on_delete=models.CASCADE)
class Doctor(models.Model):
    user = models.OneToOneField(customUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    profile_pic = models.ImageField(upload_to='profile_pics/')
    speciality = models.CharField(max_length=100, choices=customUser.SPECIALITY_CHOICES)
class BlogPost(models.Model):
    CATEGORY_CHOICES = [
        ('Mental Health', 'Mental Health'),
        ('Heart Disease', 'Heart Disease'),
        ('Covid19', 'Covid19'),
        ('Immunization', 'Immunization'),
        # Add more categories as needed
    ]

    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    summary = models.TextField()
    content = models.TextField()
    author = models.ForeignKey(customUser, on_delete=models.CASCADE)
    is_draft = models.BooleanField()

    def __str__(self):
        return self.title

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"Appointment with {self.doctor} on {self.date} from {self.start_time} to {self.end_time}"





