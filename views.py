from django.shortcuts import render, redirect
from.models import *
from.forms import StudentRegistration
from.forms import SInformation
from django.contrib.auth.forms import UserCreationForm
from .forms import  CreateUserForm, SInformation
from datetime import date, time
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .decorators import unauthenticated_user, allowed_users, admin_only

# Create your views here.
@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='stud')
            user.groups.add(group)
            messages.success(request, 'Account was created for ' + username)
            return redirect('login')
    context = {'form':form}
    return render(request, 'core/register.html', context)
		
@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password =request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.info(request, 'Username OR password is incorrect')
    context = {}
    return render(request, 'core/login.html', context)
    	

def logoutUser(request):
	logout(request)
	return redirect('login')

@login_required(login_url='login')
@admin_only
def dashboard(request):
    stud = Student.objects.all()
    total_leaves = stud.filter(status__exact='leave').count()
    presents = stud.filter(status__exact='present').count()
    absensts = stud.filter(status__exact='absent').count()
    context = {'total_leaves':total_leaves, }
    if request.method == 'POST':   
          fm = StudentRegistration(request.POST)
          if fm.is_valid():
            fm.save()  
    else:
        fm = StudentRegistration()
    stud = Student.objects.filter(date_created__date__gt=date(2020,12,24))
    print ("SQL Query:", stud.query)
    fm = StudentRegistration()
    return render(request, 'core/dashboard.html',{'form': fm, 'stu': stud,'total_leaves':total_leaves, 'presents':presents, 'absensts':absensts })
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def  update_data(request, id):
    if request.method == 'POST':
        pi = Student.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance = pi)
        if fm.is_valid():
          fm.save()
    else:
         pi= Student.objects.get(pk=id)
         fm = StudentRegistration(instance=pi)
    return render(request, 'core/updatestudent.html',{'form':fm,})
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def delete_data(request, id):
    if request.method == 'POST':
     pi = Student.objects.get(pk=id)
    pi.delete()
    return HttpResponseRedirect('/')
@login_required(login_url='login')
def attendence(request):
    

 
    if request.method == 'POST':       
          fm = SInformation(request.POST)
          if fm.is_valid():
            fm.save()
    else:
        fm = SInformation()
    stud = Attend.objects.all()

    fm = SInformation()
    return render(request, 'core/attendence.html', { 'form': fm,'stu': stud})