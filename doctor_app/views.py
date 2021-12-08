from django.shortcuts import render,redirect
from .models import *
from .forms import *
import random
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

default_dict = {
    "acc_page":["login_page","register_page","recover_pwd_page"],
    "courses" :[course for course in Course.objects.all()]
}

def otp(request, otp_for=None):
    otp_num = random.randint(1000, 9999)
    print('OTP is :', otp_num)
    request.session['otp'] = otp_num

    email_to_list = [request.session['email'],]

    subject = f'otp for {otp_for} Registration'

    email_from = settings.EMAIL_HOST_USER

    message = f'Your one time password varification is :{otp_num}.'

    send_mail(subject,message,email_from,email_to_list)

def index(request):
    default_dict['current_page'] = 'index'
    return render(request, 'index.html',default_dict)
    
def profile_page(request):
    profile_data(request)
    default_dict['current_page'] = 'profile_page'
    return render(request, 'profile_page.html',default_dict)

def profile_setting_page(request):
    default_dict['current_page'] = 'profile_setting_page'
    return render(request, 'profile_setting_page.html',default_dict)

def login_page(request):
    default_dict['current_page'] = 'login_page'
    return render(request, 'login_page.html',default_dict)

def otp_page(request):
    default_dict['current_page'] = 'otp_page'
    return render(request, 'otp_page.html', default_dict)

def register_page(request):
    default_dict['current_page'] = 'register_page'
    default_dict['roles'] = [role for role in Role.objects.all()]
    return render(request, 'register_page.html', default_dict)

def register(request):

    role = Role.objects.get(id=int(request.POST['role']))
    request.session['email'] = request.POST['email']

    master = Master.objects.create(
        Role = role,
        Email = request.POST['email'],
        Password = request.POST['password']
    )
    if role.Name == 'student':
        course = Course.objects.get(id=int(request.POST['course']))
        
        Student.objects.create(
            Master = master,
            Course = course,
        )
    else:
        Faculty.objects.create(
            Master = master,
        )
    otp(request , role.Name)
    
    return redirect(otp_page)

def login(request):
    master = Master.objects.get(Email=request.POST['email'])

    if master.Password  == request.POST['password']:
        request.session['email'] = master.Email
        if master.IsActive:
            return redirect(profile_page)
        else:
            otp(request, master.Role.Name)
            return redirect(otp_page)
    else:
        return redirect(index)

def varify_otp(request):
    email = request.session['email']

    if request.session['otp'] == int(request.POST['otp']):
        master = Master.objects.get(Email=email)
        master.IsActive = True
        master.save()
    else:
        print('Invalid OTP...')
        return redirect(register_page)

    return redirect(login_page)

def profile_data(request):

    master = Master.objects.get(Email=request.session['email'])

    if master.Role.Name == 'student':
        user = Student.objects.get(Master = master)
    else:
        user = Faculty.objects.get(Master = master)

    default_dict['user_profile'] = user

def profile_update(request):
    user = default_dict['user_profile']
    user_role = user.Master.Role.Name

    full_name = request.POST['fullname']
    mobile = request.POST['mobile']
    dob = request.POST['dob']
    gender = request.POST['gender']

    if user_profile == 'student':
        user = Student.objects.get(id=user.id)
    elif user_profile == 'faculty':
        user = Faculty.objects.get(id=user.id)

    user.FullName = full_name
    user.Mobile = mobile
    user.Dob = dob
    user.Gender = gender

    user.save()

    return redirect(profile_page)

def sign_out(request):
    if 'email' in request.session:
        del request.session['email']
    return redirect(login_page)