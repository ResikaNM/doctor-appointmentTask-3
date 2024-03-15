from django.shortcuts import render, redirect
from .forms import signupform,loginForm,BlogPostForm,AppointmentForm
from django.contrib.auth import authenticate,login
from .models import Patient,Doctor,customUser,BlogPost
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta

# from google.oauth2.credentials import Credentials
# from google.auth.transport.requests import Request
# from googleapiclient.discovery import build

# import pytz
# Create your views here.
def signupView(request):
    if request.method=='POST':
        form=signupform(request.POST,request.FILES)
        if form.is_valid():
            user=form.save()
            if form.cleaned_data['is_patient']:
                user.is_patient=True
                patient=Patient.objects.create(user=user)
            elif form.cleaned_data['is_doctor']:
                user.is_doctor = True
                doctor = Doctor.objects.create(
                    user=user,
                    name=form.cleaned_data['first_name'],  # Assuming 'name' is a field in your signup form for doctors
                    profilepic=form.cleaned_data['profile_pic'],
                    # Assuming 'profilepic' is a field in your signup form for doctors
                    speciality=form.cleaned_data['speciality']
                    # Assuming 'speciality' is a field in your signup form for doctors
                )
            user.save()
            login(request,user)
            return redirect('login')

    else:
        form=signupform()
    return render(request,'signup.html',{'form':form})

def loginView(request):
    if request.method=='POST':
        form=loginForm(request,data=request.POST)
        if form.is_valid():
           user=form.get_user()
           login(request,user)
           if user.is_patient:
            return redirect('Patient_Dashboard')
           elif user.is_doctor:
               return redirect('Doctor_Dashboard')

    else:
        form=loginForm()
    return render(request,'login.html',{'form':form})

@login_required()
def dashboard(request):
    user=request.user
    if user.is_patient:
        return render(request,'patient.html',{'user':user})
    elif user.is_doctor:
        return render(request,'doctor.html',{'user':user})
def blog_list(request):
    posts=BlogPost.objects.filter(is_draft=False)
    print("hiii")
    return render(request,'blog_list.html',{'posts':posts})

def blog_detail(request,pk):
    post=BlogPost.objects.get(pk=pk)
    return render(request,'blog_detail.html',{'post':post})

@login_required
def create_blog_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.author = request.user
            blog_post.save()
            return redirect('blog_list')
    else:
        form = BlogPostForm()
    return render(request, 'create_blog_post.html', {'form': form})

def list_doctors(request):
    doctors = Doctor.objects.all()
    return render(request, 'list_doctors.html', {'doctors': doctors})
def book_appointment(request, doctor_id):
    doctor = Doctor.objects.get(pk=doctor_id)
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.doctor = doctor
            start_time = form.cleaned_data['start_time']
            start_time=str(start_time)
            print(start_time)
            duration = timedelta(minutes=45)
            duration=str(duration)
            print(duration)
            start_time = datetime.strptime(start_time, "%H:%M:%S").time()
            duration = timedelta(hours=int(duration.split(':')[0]), minutes=int(duration.split(':')[1]),
                                 seconds=int(duration.split(':')[2]))
            end_time = (datetime.combine(datetime.today(), start_time) + duration).time()
            appointment.start_time = start_time  # Extract time
            appointment.end_time = end_time
            appointment.save()
            # create_google_calendar_event(appointment)
            return render(request, 'appointment_confirmation.html', {'appointment': appointment})
    else:
        form = AppointmentForm()
    return render(request, 'book_appointment.html', {'form': form, 'doctor': doctor})

# for api view
# from google.oauth2 import service_account
# from googleapiclient.discovery import build
#
# def book_appointment(request):
#
#     doctor_id = request.POST.get('doctor_id')
#     speciality = request.POST.get('speciality')
#     appointment_date = request.POST.get('date')
#     start_time = request.POST.get('start_time')
#     end_time=request.POST.get('end_time')
#     doctor_name=request.POST.get('name')
#
#
#     #  Google Calendar event
#     credentials = service_account.Credentials.from_service_account_file('path/to/your/credentials.json')
#     service = build('calendar', 'v3', credentials=credentials)
#
#     event = {
#         'summary': f'Appointment department {speciality}',
#         'start': {
#             'dateTime': start_time.isoformat(),
#             'timeZone': 'Asia/Kolkata',
#         },
#         'end': {
#             'dateTime': end_time.isoformat(),
#             'timeZone': 'Asia/Kolkata',
#         },
#         # Add more event details as needed
#     }
#
#     calendar_id = 'doctor_id'
#     event = service.events().insert(calendarId=calendar_id, body=event).execute()
#
#     # Display appointment details to the patient
#     appointment_details = {
#         'doctor_name': doctor_name,
#         'appointment_date': appointment_date,
#         'start_time': start_time,
#         'end_time': end_time,
#     }
#
#     return render(request, 'appointment_confirmation.html', {'appointment_details': appointment_details})








