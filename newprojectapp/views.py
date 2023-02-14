from django.contrib import messages
from django.contrib.auth import authenticate, login

from django.contrib.auth.decorators import login_required


from django.shortcuts import render, redirect

from newprojectapp.form import loginregister, studentform, parentform


# Create your views here.


def new(request):
    return render(request,'first.html')



def log(request):
    if request.method == 'POST':
        username=request.POST.get('uname')
        password=request.POST.get('pass')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            if user.is_staff:
                return redirect('adminpage')
            elif user is not None and user.is_student:
                if user.student.approval_status==True:
                    login(request,user)
                    return redirect('studentpage')
            elif user is not None and user.is_parent:
                if user.parent.approval_status==True:
                    login(request,user)
                    return redirect('parentpage')
            else:
                messages.info(request,'invalid credentials')
    return render(request,'login.html')



def signstudent(request):
    u_form = loginregister()
    s_form = studentform()
    if request.method == 'POST':
        u_form = loginregister(request.POST)
        s_form = studentform(request.POST,request.FILES)
        if u_form.is_valid() and s_form.is_valid():
            user = u_form.save(commit=False)
            user.is_student = True
            user.save()
            student = s_form.save(commit=False)
            student.user = user
            student.save()
            messages.info(request, 'student registered successfully')
            return redirect('log')
    return render(request, 'signup.html', {'s_form': s_form, 'u_form': u_form})


def psign(request):
    u_form = loginregister()
    p_form = parentform()
    if request.method == 'POST':
        u_form = loginregister(request.POST)
        p_form = parentform(request.POST)
        if u_form.is_valid() and p_form.is_valid():
            user = u_form.save(commit=False)
            user.is_parent = True
            user.save()
            parent = p_form.save(commit=False)
            parent.user = user
            parent.save()
            messages.info(request, 'parent registered successfully')
            return redirect('log')
    return render(request, 'parentsignup.html', {'s_form': p_form, 'u_form': u_form})

@login_required(login_url='log')
def adminpage(request):
    return render(request,'adminpage.html')

@login_required(login_url='log')
def studentpage(request):
    return render(request,'student.html')

@login_required(login_url='log')
def parentpage(request):
    return render(request,'parent.html')






