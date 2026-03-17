from django.http import HttpResponse
from django.shortcuts import render, redirect
from pyexpat.errors import messages

from .service.user_service import UserService


def test_ors(request):
    return HttpResponse("Hello Django....!!!!")


def welcome(request):
    return render(request, 'welcome.html')


def sing_up(request):
    print("Sing up page")
    message = ''
    if request.method == "POST":
        params = {}
        params['firstName'] = request.POST.get('firstName')
        params['lastName'] = request.POST.get('lastName')
        params['loginId'] = request.POST.get('loginId')
        params['password'] = request.POST.get('password')
        params['dob'] = request.POST.get('dob')
        params['address'] = request.POST.get('address')
        service = UserService()
        service.add(params)
        message = 'Data Add Successfully'

    return render(request, 'registration.html', {'message': message})


def singIn(request):
    print("Sing IN page")
    message = ''
    if request.method == 'POST':
        if request.POST.get('operation') == "signIn":
            loginId = request.POST.get('loginId')
            password = request.POST.get('password')
            service = UserService()
            User_data = service.auth(loginId, password)
            if len(User_data) != 0:
                request.session['firstName'] = User_data[0].get('firstName')

                return redirect("/ors/welcome/")
            else:
                message = "Invalid LoginId or Password"

    if request.POST.get('operation') == "signUp":
        return redirect("/ors/singUp/")
    return render(request, 'login.html', {'message': message})


def logout(request):
    request.session['firstName'] = None

    return redirect("/ors/singIn/")


def test_list(request):
    list = [
        {"id": 1, "firstName": "abc", "lastName": "aaa", "email": "abc@gmail.com", "password": "12345"},
        {"id": 2, "firstName": "xyz", "lastName": "aaa", "email": "abc@gmail.com", "password": "12345"},
        {"id": 3, "firstName": "pqr", "lastName": "aaa", "email": "abc@gmail.com", "password": "12345"}
    ]
    return render(request, "testlist.html", {"list": list})
