from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
from django.core.mail import *
from django.conf import settings
import random
from django.contrib.auth import update_session_auth_hash
import string
from django.core.mail import send_mail
from django.conf import settings


def index(request):
    return render(request, 'user_login\index.html')


def login(request,):
    return render(request, 'user_login\logIn.html')


def signUp(request):
    if request.method == 'POST':
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        birth_date = request.POST.get("birth_date")
        gender = request.POST.get("gender")
        # userdata = userinfo(first_name=first_name, last_name=last_name, email=email, username=username,
        #                    password1=password1, password2=password2, birth_date=birth_date, gender=gender)
        if len(first_name) != 0 and len(last_name) != 0:
            if len(username) != 0:
                if User.objects.filter(username=username).exists():
                    messages.error(
                        request, "This username already exists! Please try another one.")
                else:
                    if len(email) != 0:
                        if User.objects.filter(email=email).exists():
                            messages.error(
                                request, "This email already exists! Please try another one.")
                        else:
                            if len(password1) >= 5:
                                if password1 == password2:
                                    if len(birth_date) != 0:
                                        if len(gender) != 0:
                                            userdata = userinfo.objects.create(
                                                first_name=first_name, last_name=last_name, username=username, email=email, password1=password1, password2=password2, birth_date=birth_date, gender=gender)
                                            userdata.save()
                                            messages.success(
                                                request, 'Account has been created')
                                            return render(request, 'user_login\\user_verify.html')
                                        else:
                                            messages.error(
                                                request, "Please select your Gender!")
                                    else:
                                        messages.warning(
                                            request, "Please enter your birth date.")
                                else:
                                    messages.error(
                                        request, "Confirm password does not matched.")
                            else:
                                messages.error(
                                    request, 'Password must be at least 6 characters long!')
                    else:
                        messages.warning(request, "Enter your Mail address.")
            else:
                messages.warning(request, "Enter your username.")
        else:
            messages.warning(request, "Enter Your name correctly.")
    return render(request, 'user_login\signUp.html')


def user_verify(request):

    otp_code = random.randint(13575, 94765)
    if request.method == 'POST':
        email = request.POST.get('email')

    return render(request, 'user_verify')


def send_mail_registration(email, otp_code):
    subject = "Account Verification OTP"
    message = f'Your FRIENDLLY account verification OTP is :  {otp_code}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)
