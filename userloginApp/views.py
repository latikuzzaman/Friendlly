from django.shortcuts import render, redirect


def index(request):
    return render(request, 'user_login\index.html')


def login(request):
    return render(request, 'user_login\logIn.html')


def signUp(request):
    return render(request, 'user_login\signUp.html')


def signUP_verification(request):
    if request.method == 'POST':
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        birth_date = request.POST.get("birth_date")
        gender = request.POST.get("gender")

    return render(request, 'user_login\signUP_verification')
