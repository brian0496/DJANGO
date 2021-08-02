from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Conte, Cliente, Estado
from .forms import login_frm
# Create your views here.

import datetime
now = datetime.datetime.now()
today = now.strftime('%Y-%m-%d')

def main_page(request):
    if request.method == "POST":
        f = login_frm(request.POST)
        if f.is_valid():
            user_log = f.cleaned_data['user']
            passw_log = f.cleaned_data['passw']
            if Cliente.objects.filter(usuario = user_log):
                if Cliente.objects.filter(pasw = passw_log):
                    return HttpResponseRedirect('home/')
                else:
                    f = login_frm()
                    return render(request,'app/login.html',{'frmlogin':f})

    else:
        f = login_frm()
        return render(request,'app/login.html',{'frmlogin':f})
    return render(request,'app/index.html',{'frmlogin':f}) 

def home_page(request):
    if request.method=="GET":
        receive = dict(request.GET)
        title = receive.get('title')
        text = receive.get('text')
        user = receive.get('autor')
        #print(title, text)
        if title != None:
            conte = Conte(titulo= title, text= text, user= user, fecha= today)
            conte.save()
        
    return render(request,'app/home.html',{})

def publications_page(request):
    lista_datos = Conte.objects.all()
    return render(request,'app/publications.html',{'lista':lista_datos})