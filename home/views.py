from django.shortcuts import render
from django.template import loader
from features.models import Members
#from .forms import UserLogin,UserReg
from django.contrib import auth
from django.contrib.auth import authenticate,login
from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'features/home.html')

