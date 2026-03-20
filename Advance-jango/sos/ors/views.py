from cgi import parse_multipart

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


def Add(request):
    print("Add up page")
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
        if request.POST['operation'] == "save":
            service.add(params)
            message = 'User Added Successfully'
        if request.POST['operation'] == "update":
            params['id'] = int(request.POST.get('id', 0))
            service.update(params)
            message = 'Data Updated Successfully'

    return render(request, 'AddUser.html', {'message': message})


def user_list(request):
    params = {}
    params['pageNo'] = 1
    params['pageSize'] = 5
    if request.method == "POST":
        if request.POST['operation'] == "next":
            params['pageNo'] = int(request.POST['pageNo'])
            params['pageNo'] += 1
        if request.POST['operation'] == "previous":
            params['pageNo'] = int(request.POST['pageNo'])
            params['pageNo'] -= 1
        if request.POST['operation'] == "search":
            params['firstName'] = request.POST['firstName']

    service = UserService()
    list = service.search(params)
    index = (params['pageNo'] - 1) * 5
    return render(request, "userlist.html", {"list": list, 'pageNo': params['pageNo'], 'index': index})


def delete_user(request, id):
    service = UserService()
    service.delete(id)
    return redirect("/ors/userlist/")


def edit_user(request, id=0):
    service = UserService()
    user_data = service.get(id)
    user_data[0]['dob'] = user_data[0]['dob'].strftime('%Y-%m-%d')
    return render(request, 'Adduser.html', {'form': user_data[0]})