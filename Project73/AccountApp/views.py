from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def registerview(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    template_name = 'AccountApp/register.html'
    context = {'form':form}
    return render(request, template_name, context)


def loginview(request):
    print('view called')
    if request.method == 'POST':
        unm = request.POST.get('un')
        pwd = request.POST.get('pw')
        print(unm,pwd)
        user = authenticate(username=unm, password=pwd)
        print(user)
        if user is not None:
            print('login success')
            login(request, user)
            return redirect('show')
        else:
            print('check credentials')
            messages.error(request, 'Invalid Credentials')
    template_name = 'AccountApp/login.html'
    context = {}
    return render(request, template_name, context)


def logoutview(request):
    logout(request)
    return redirect('login')
