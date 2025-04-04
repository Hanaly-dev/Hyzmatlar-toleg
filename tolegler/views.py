from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from .forms import*
from .models import *
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from datetime import datetime
from django.db.models import Sum


def index(request):
    habarlar = Habarlar.objects.all()
    context={
        'habarlar': habarlar
    }
    return render(request, 'tolegler/index.html',context)

def biz_barada(request):
    habarlar = Habarlar.objects.all()
    context={
        'habarlar': habarlar
    }
    return render(request, 'tolegler/biz_barada.html',context)

def hyzmatlar(request):
    hyzmatlar=Hyzmat.objects.all()
    habarlar = Habarlar.objects.all()
    context={
        'habarlar': habarlar,
        'hyzmatlar': hyzmatlar
    }
    return render(request, 'tolegler/hyzmatlar.html',context)
def habarlasmak(request):
    habarlar=Habarlar.objects.all()
    context={
        'habarlar': habarlar
    }
    return render(request, 'tolegler/habarlasmak.html',context)
def tolegler(request):
    now = datetime.now
    tolegler = Toleg.objects.filter(ulanyjy=request.user)
    habarlar=Habarlar.objects.all()
    bugun = now().date()
    aylik_baslangyc = now().replace(day=1).date()
    yyl_baslangyc = now().replace(month=1, day=1).date()

    bugunki_jemi = tolegler.filter(senesi=bugun).aggregate(Sum('mukdar'))['mukdar__sum'] 
    aylik_jemi = tolegler.filter(senesi__gte=aylik_baslangyc).aggregate(Sum('mukdar'))['mukdar__sum'] 
    yyllyk_jemi = tolegler.filter(senesi__gte=yyl_baslangyc).aggregate(Sum('mukdar'))['mukdar__sum'] 
    umumy_mukdar = tolegler.aggregate(Sum('mukdar'))['mukdar__sum']

    return render(request, 'tolegler/toleglerim.html', {
        'tolegler': tolegler,
        'bugunki_jemi': bugunki_jemi,
        'aylik_jemi': aylik_jemi,
        'yyllyk_jemi': yyllyk_jemi,
        'umumy_mukdar': umumy_mukdar,
        'habarlar': habarlar
    })

def toleg_etmek(request):
    if request.method == "POST":
        mukdar = request.POST.get('mukdar')
        hyzmat_id = request.POST.get('hyzmat')
        toleg_usuly = request.POST.get('toleg_usuly')

        Toleg.objects.create(
            ulanyjy=request.user,
            hyzmat_id=hyzmat_id,
            mukdar=mukdar,
            toleg_usuly=toleg_usuly
        )

        return redirect('tolegler')  

    hyzmatlar = Hyzmat.objects.all()
    habarlar=Habarlar.objects.all()
    context={
        'hyzmatlar': hyzmatlar,
        'habarlar': habarlar
    }
    return render(request, 'tolegler/toleg_etmek.html', context)
    
def loginView(request):
    if request.method == 'POST':
        email = request.POST.get('email') 
        password = request.POST.get('password') 

        if not email or not password:
            messages.error(request, "Maglumatlary doly girizmeli!")
            return redirect('login')

        try:
            
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, "E-mail salgyňyz ýalňyş")
            return redirect('login')  
        user = authenticate(request, username=user.username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            next_url = request.GET.get('next', 'index')  
            return redirect(next_url)  
        
        messages.error(request, "Ulanyjy hasaby ýok!")
        return redirect('login')  

    return render(request, 'tolegler/login.html')  


def logoutView(request):
    logout(request)
    return redirect('index')


def registerView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')  
        password = request.POST.get('password')  
        confirm_password = request.POST.get('confirm_password')  
        if not email or not password or not username:
            messages.error(request, _("Maglumatlary doly girizmeli"))
            return redirect('register')

        if password != confirm_password:
            messages.error(request, _("Parollar bir-birine deň bolmaly"))
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, _("Bu e-mail salgy üçin hasap döredilen"))
            return redirect('register')
        if User.objects.filter(username=username).exists():
            messages.error(request, _("Bu ulanyjy ady üçin hasap döredilen"))
            return redirect('register')
        
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        messages.success(request, _("Hasap döredildi"))
        return redirect('login')  

    return render(request, 'tolegler/register.html')

def profil_view(request):
    profil = Profil.objects.get(ulanyjy=request.user)
    habarlar=Habarlar.objects.all()
    return render(request, 'tolegler/profil.html', {'profil': profil, 'habarlar': habarlar})



def hasabatlar_view(request):
    now = datetime.now()
    tolegler = Toleg.objects.filter(ulanyjy=request.user)
    gunlik=tolegler.filter(senesi__day=now.day).aggregate(Sum('mukdar'))
    aylik = tolegler.filter(senesi__month=now.month).aggregate(Sum('mukdar'))
    yyllyk = tolegler.filter(senesi__year=now.year).aggregate(Sum('mukdar'))
    return render(request, 'hasabatlar.html', {'aylyk': aylik, 'yyllyk': yyllyk,'gunlik':gunlik, 'tolegler': tolegler})

