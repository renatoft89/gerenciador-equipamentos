from django.shortcuts import render
from django.http import HttpResponse


def cadastro(request):
    if request == "GET":
        return render(request, 'cadastro.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        return HttpResponse(username)


def login(request):
    return render(request, 'login.html')
