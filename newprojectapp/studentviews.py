
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from newprojectapp.models import  hostel,food,fee,attendance,notification,payment,complaint,booking,Stud_reg,review,payment
from django.shortcuts import render,redirect

from django.contrib.auth import logout

from newprojectapp.form import complaintform,bookingform,studentform,reviewform,paymentform

@login_required(login_url='log')
def view_stud_hostel(request):
    data = hostel.objects.all()
    return render(request, 'viewstudhostel.html', {'data': data})

@login_required(login_url='log')
def view_stud_food(request):
    data = food.objects.all()
    return render(request, 'viewstudfood.html', {'data': data})

@login_required(login_url='log')
def view_stud_fee(request):
    data = fee.objects.all()
    return render(request, 'viewstudfee.html', {'data': data})

@login_required(login_url='log')
def view_stud_notification(request):
    data = notification.objects.all()
    return render(request, 'viewstudnoti.html', {'data': data})

@login_required(login_url='log')
def view_stud_attendance(request):
    u = Stud_reg.objects.get(user=request.user)
    data = complaint.objects.filter(name=u)
    return render(request, 'viewstudatt.html', {'data': data})


@login_required(login_url='log')
def add_complaint(request):
    form=complaintform()
    u=request.user
    if request.method=="POST":
        form=complaintform(request.POST)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.user=u
            obj.save()
            return redirect('view_stud_complaint')
    return render(request,'addcomplaint.html',{'form':form})

@login_required(login_url='log')
def view_stud_complaint(request):
    u=Stud_reg.objects.get(user=request.user)
    data = complaint.objects.filter(user=request.user)
    return render(request, 'viewstudcomplaint.html', {'data': data})




@login_required(login_url='log')
def add_booking(request):
    form=bookingform()
    if request.method=="POST":
        form=bookingform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_stud_booking')
    return render(request,'addstudbooking.html',{'form':form})

@login_required(login_url='log')
def view_stud_booking(request):
    data = booking.objects.all()
    return render(request, 'viewstudbookig.html', {'data': data})

@login_required(login_url='log')
def booking_update(request,id):
    booking1=booking.objects.get(id=id)
    form=bookingform(instance=booking1)
    if request.method=="POST":
        form=bookingform(request.POST,instance=booking1)
    if form.is_valid():
        form.save()
        return redirect('view_stud_booking')
    return render(request,'addstudbooking.html',{'form':form})

@login_required(login_url='log')
def booking_delete(request,id):
    booking.objects.get(id=id).delete()
    return redirect('view_stud_booking')

@login_required(login_url='log')
def add_review(request):
    form=reviewform()
    if request.method=="POST":
        form=reviewform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_stud_review')
    return render(request,'addreview.html',{'form':form})

@login_required(login_url='log')
def view_stud_review(request):
    u = Stud_reg.objects.get(user=request.user)
    data = review.objects.filter(name=u)
    return render(request, 'viewstudreview.html', {'data': data})



@login_required(login_url='log')
def profile_view(request):
    student = Stud_reg.objects.get(user=request.user)
    return render(request,'studprofileview.html',{'student':student})

@login_required(login_url='log')
def profile_update(request):
    profile1=Stud_reg.objects.get(user=request.user)
    form=studentform(instance=profile1)
    if request.method=="POST":
        form=studentform(request.POST,request.FILES,instance=profile1)
    if form.is_valid():
        form.save()
        return redirect('profile_view')
    return render(request,'profileupdate.html',{'form':form})

@login_required(login_url='log')
def logout_view(request):
    logout(request)
    return redirect('log')

@login_required(login_url='log')
def delete_profile_student(request):
    user =request.user
    if request.method=='POST':
        user.delete()
        messages.info(request,'Your Account Deleted Successfully')
        return redirect('log')
    return render(request,'studentdelete_profile.html')

def cancel_profile_student(request):
    return redirect('profile_view')



@login_required(login_url='log')
def view_stud_pay(request):
    u = Stud_reg.objects.get(user=request.user)
    data = payment.objects.filter(studentname=u)
    return render(request, 'viewstudpay.html', {'data': data})


@login_required(login_url='log')
def approve_payment(request,id):
    pay1=payment.objects.get(id=id)
    pay1.status = 1
    pay1.save()
    messages.info(request,"student paid succesfully")
    return redirect('view_stud_pay')


@login_required(login_url='log')
def reject_payment(request,id):
    pay1=payment.objects.get(id=id)
    pay1.status = 2
    pay1.save()
    messages.info(request,"not paid")
    return redirect('view_stud_pay')









