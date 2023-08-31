from typing import Any
from django.shortcuts import render, redirect
from django.urls import reverse

from django.http import HttpResponse
from django.views.generic import View
from .models import Userprofile
from .forms import User_profile, User_profile_info
from django.contrib.auth import authenticate, login as auth_login, logout


class Register(View):

    def get(self, request):
        form = User_profile()
        form_info = User_profile_info()
        return render(request, 'register.html', {'form': form, 'frominfo': form_info})

    def post(self, request):
        # username = ''
        # password = ''
        # password2 = ''
        userprofile = User_profile()
        userprofileinfo = User_profile_info()

        if userprofile.is_valid() and userprofileinfo.is_valid():
            userprofile = User_profile(data=request.POST)
            user = userprofile.save(commit=False)
            # username = user.cleaned_data.get('username')
            # password = user.cleaned_data.get('password')
            # password2 = user.cleaned_data.get('password2')
            # if password2==password:

            # userexist = Userprofile.objects.get(username=username)
            # if userexist:
            #     return render(request, 'register.html', {'context':"User is already created"})
            # else:
            user.set_password(user.password)
            user.save()
            userprofileinfo = User_profile_info(data=request.POST)
            userinfo = userprofileinfo.save(commit=False)
            userinfo.user = user
            if 'picture' in request.FILES:
                userinfo.picture = request.FILES["picture"]
            userinfo.save()
            # else:
            #     return render(request, 'register.html', {'context':"password is not match"})
            Userprofile.object.get_or_create(user=userinfo.user)

        return render(request, 'register.html', {'form': userprofile, 'frominfo': userprofileinfo, 'users': Userprofile.objects.all()
})


class Login(View):
    def get(self, request):
        form = User_profile()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                auth_login(request, user)
                return redirect(reverse('base'))
            else:
                return HttpResponse("user is not active")

        else:
            return HttpResponse('invalid data')


def base(request):
    return render(request, 'base.html')
