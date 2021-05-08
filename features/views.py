from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db.models import Max
from django.template import loader
from .models import Members
from .forms import Trsc,Usearch,AddR,AddST,AddT,AddRT
import json

from home.models import RouteStation,Station,Route,Trains,Reservation,Add_Train
def getTrains(request):
    if request.method=='POST':
        form=Usearch(request.POST)
        if form.is_valid():

            data=form.cleaned_data
            src=data['src']
            des=data['des']
            a=RouteStation.objects.filter(sid=des)
            x=[]
            o=0
            for i in a:
                tno=i.tno
                b=RouteStation.objects.filter(tno=tno,sid=src)
                for j in b:
                    if j.order<i.order:
                        x.append(j)
                        o=i.order-j.order

        else:
            return HttpResponse('<h1>invalid Data</h1>')
        return render(request,'features/trains.html',{'data':x,'o':o,'src':src,'des':des})
    return HttpResponse('<h1>Wrong REq</h1>')


def schedule(request):
    a=Trains.objects.all()
    return render(request,'features/schedule.html',{'a':a})

def getTinfo(request):
    form=Trsc(request.GET)
    if form.is_valid():
        data=form.cleaned_data
        tno=data['tnum']
        a=RouteStation.objects.filter(tno=tno).order_by('order')


        return render(request,'features/trinfo.html',{'data':a})

    return HttpResponse('<h1>DAta invalid<h1>')

def search(request):
    a=Station.objects.all()
    return render(request,'features/seat.html',{'a':a})


def pnr(request):
    if request.method=='POST':
        pnr=request.POST['pnr']
        a=Reservation.objects.filter(pnr=pnr)

        return render(request,'features/pnr.html',{'r':a})


    return render(request,'features/pnr.html')
