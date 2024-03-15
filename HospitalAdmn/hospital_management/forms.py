from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django import forms
from .models import customUser,BlogPost

class signupform(UserCreationForm):
    first_name=forms.CharField(max_length=30)
    second_name=forms.CharField(max_length=30)
    email=forms.EmailField(max_length=150)
    address_line1 = forms.CharField(max_length=250)
    city = forms.CharField(max_length=250)
    state = forms.CharField(max_length=250)
    pincode = forms.IntegerField()
    profile_pic = forms.ImageField(required=False)

    class Meta:
        model=customUser
        fields=('username','first_name','second_name','email','is_patient','is_doctor','speciality','address_line1','city','state','pincode','profile_pic','password1','password2')

class loginForm(AuthenticationForm):
    class Meta:
        model=customUser
        fields=['username','password']

class BlogPostForm(forms.ModelForm):
    class Meta:
        model=BlogPost
        fields=['title','image','category','summary','content','is_draft']

from django import forms
from .models import Appointment

class DateInput(forms.DateInput):
    input_type = 'date'
class TimeInput(forms.TimeInput):
    input_type = 'time'
class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['date', 'start_time']
        widgets={
            'date':DateInput(),
            'start_time': TimeInput()
        }


