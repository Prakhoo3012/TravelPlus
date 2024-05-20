from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Packages,City, Country, Customer
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm

from django.contrib.auth.models import Group

from django.contrib.auth import authenticate, login, logout 

from django.contrib import messages

from django.contrib.auth.decorators import login_required

from .decorators import unauthenticated_user, allowed_users, admin_only


# Create your views here.
def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')

    else:
        form = CreateUserForm()
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data.get('username')

                group = Group.objects.get(name='customer')
                user.groups.add(group)

                Customer.objects.create(
                    user=user
                )

                messages.success(request, 'Account was created for ' + username) 

                return redirect('login')

        context = {'form': form}
        return render(request, "register.html", context)
    
@unauthenticated_user
def loginPage(request):
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'username OR password incorrect')

        context = {}
        return render(request, "login.html", context)

def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def index(request):
    packagess = Packages.objects.all()

    q = request.GET.get('q') if request.GET.get('q') != None else ''

    packages = Packages.objects.filter(
        Q(price__icontains=q) | 
        Q(package_name__icontains=q) |
        Q(destination__city_name__icontains=q) |
        Q(destination__country__country_name__icontains=q) |
        Q(inclusions__icontains=q) 
    )
    destinations = City.objects.all()
    countries = Country.objects.all()

    context = {"packages": packages, "packagess": packagess, "destinations": destinations, "countries": countries}
    return render(request, "index.html", context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def package(request, pk):
    package = Packages.objects.get(id=pk)

    context = {"package": package}
    return render(request, "package.html", context)

@admin_only
def addPackages(request):
    context = {}
    return render(request, "addpackage.html", context)

def userPage(request):
    context = {}
    return render(request, "profile.html", context)
