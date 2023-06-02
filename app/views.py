from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.forms import *
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate

def home(request):
    return render(request,'home.html')



def registration(request):
    ufo=UserForm()
    pfo=ProfileForm()
    d={'ufo':ufo,'pfo':pfo}

    if request.method=='POST' and request.FILES:
        ufd=UserForm(request.POST)
        pfd=ProfileForm(request.POST,request.FILES)
        if ufd.is_valid() and pfd.is_valid():
            NSUO=ufd.save(commit=False)
            password=ufd.cleaned_data['password']
            NSUO.set_password(password)
            NSUO.save()

            NSPO=pfd.save(commit=False)
            NSPO.username=NSUO
            NSPO.save()


            return HttpResponse('Regsitration is Susssessfulll')
        else:
            return HttpResponse('Not valid')
    return render(request,'registration.html',d)

def change_password(request):
    if request.method=='POST':
        pw=request.POST['pw']
        username=request.session.get('username')
        UO=User.objects.get(username=username)
        UO.set_password(pw)
        UO.save()
        return HttpResponse('Password is changed successfully')
    return render(request,'change_password.html')
