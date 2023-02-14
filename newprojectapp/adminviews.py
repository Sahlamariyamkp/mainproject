from django.contrib import messages

from django.contrib.auth import logout

from django.contrib.auth.decorators import login_required

from django.http import JsonResponse

from django.shortcuts import render,redirect



from newprojectapp.models import Stud_reg,Parent_reg,hostel,food,fee,payment,notification,attendance,staff,complaint,booking,review

from newprojectapp.form import hostelform,foodform,paymentform,notificationform,attendanceform,staffform,replayform,feeform

@login_required(login_url='log')
def sview(request):
    data=Stud_reg.objects.all()
    return render(request,'stuview.html',{'data':data})

@login_required(login_url='log')
def pview(request):
    data=Parent_reg.objects.all()
    return render(request,'pview.html',{'data':data})

@login_required(login_url='log')
def approve_student(request,id):
    student1=Stud_reg.objects.get(user_id=id)
    student1.approval_status=1
    student1.save()
    messages.info(request,"student approved succesfully")
    return redirect('sview')

@login_required(login_url='log')
def reject_student(request,id):
    student1=Stud_reg.objects.get(user_id=id)
    # if request.method=='POST':
    student1.approval_status = 2
    student1.save()
    messages.info(request,"Rejected student registration")
    return redirect('sview')


@login_required(login_url='log')
def approve_parent(request,id):
    parent1=Parent_reg.objects.get(user_id=id)
    parent1.approval_status=1
    parent1.save()
    messages.info(request,"parent approved successfully")
    return redirect('pview')


@login_required(login_url='log')
def reject_parent(request,id):
    parent1=Parent_reg.objects.get(user_id=id)
    parent1.approval_status=2
    parent1.save()
    messages.info(request,"Rejected parent registration")
    return redirect('pview')


@login_required(login_url='log')
def add_hostel(request):
    form=hostelform()
    if request.method=="POST":
        form=hostelform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_hostel')
    return render(request,'addhostel.html',{'form':form})



@login_required(login_url='log')
def view_hostel(request):
    data = hostel.objects.all()
    return render(request, 'viewhostel.html', {'data': data})


@login_required(login_url='log')
def add_food(request):
    form = foodform()
    if request.method == "POST":
        form = foodform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_food')
    return render(request, 'addfood.html', {'form': form})


@login_required(login_url='log')
def view_food(request):
    data = food.objects.all()
    return render(request, 'viewfood.html', {'data': data})


@login_required(login_url='log')
def add_fee(request):
    form = feeform()
    if request.method == "POST":
        form = feeform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_fee')
    return render(request, 'addfee.html', {'form': form})


@login_required(login_url='log')
def view_fee(request):
    data = fee.objects.all()
    return render(request, 'viewfee.html', {'data': data})


@login_required(login_url='log')
def add_admin_pay(request):
    form = paymentform()
    if request.method == "POST":
        form = paymentform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_pay')
    return render(request, 'addadminpay.html', {'form': form})


@login_required(login_url='log')
def view_pay(request):
    data = payment.objects.all()
    return render(request, 'viewpay.html', {'data': data})







@login_required(login_url='log')
def add_notification(request):
    form = notificationform()
    if request.method == "POST":
        form = notificationform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_notification')
    return render(request, 'addnotification.html', {'form': form})

@login_required(login_url='log')
def view_notification(request):
    data = notification.objects.all()
    return render(request, 'viewnotification.html', {'data': data})


@login_required(login_url='log')
def add_attendance(request):
    form = attendanceform()
    if request.method == "POST":
        form = attendanceform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_attendance')
    return render(request, 'addattendance.html', {'form': form})



@login_required(login_url='log')
def view_attendance(request):
    data = attendance.objects.all()
    return render(request, 'viewattendance.html', {'data': data})


@login_required(login_url='log')
def add_staff(request):
    form = staffform()
    if request.method == "POST":
        form = staffform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_staff')
    return render(request, 'addstaff.html', {'form': form})

@login_required(login_url='log')
def view_staff(request):
    data = staff.objects.all()
    return render(request, 'viewstaff.html', {'data': data})


@login_required(login_url='log')
def hostel_update(request,id):
    hostel1=hostel.objects.get(id=id)
    form=hostelform(instance=hostel1)
    if request.method=="POST":
        form=hostelform(request.POST,request.FILES,instance=hostel1)
    if form.is_valid():
        form.save()
        return redirect('view_hostel')
    return render(request,'addhostel.html',{'form':form})


@login_required(login_url='log')
def hostel_delete(request,id):
    hostel.objects.get(id=id).delete()
    return redirect('view_hostel')


@login_required(login_url='log')
def food_update(request,id):
    food1=food.objects.get(id=id)
    form=foodform(instance=food1)
    if request.method=="POST":
        form=foodform(request.POST,instance=food1)
    if form.is_valid():
        form.save()
        return redirect('view_food')
    return render(request,'addfood.html',{'form':form})


@login_required(login_url='log')
def food_delete(request,id):
    food.objects.get(id=id).delete()
    return redirect('view_food')


@login_required(login_url='log')
def fee_update(request,id):
    fee1=fee.objects.get(id=id)
    form=feeform(instance=fee1)
    if request.method=="POST":
        form=feeform(request.POST,instance=fee1)
    if form.is_valid():
        form.save()
        return redirect('view_fee')
    return render(request,'addfee.html',{'form':form})


@login_required(login_url='log')
def fee_delete(request,id):
    fee.objects.get(id=id).delete()
    return redirect('view_fee')


@login_required(login_url='log')
def pay_update(request,id):
    payment1=payment.objects.get(id=id)
    form=paymentform(instance=payment1)
    if request.method=="POST":
        form=paymentform(request.POST,instance=payment1)
    if form.is_valid():
        form.save()
        return redirect('view_pay')
    return render(request,'addadminpay.html',{'form':form})


@login_required(login_url='log')
def pay_delete(request,id):
    payment.objects.get(id=id).delete()
    return redirect('view_pay')


@login_required(login_url='log')
def notification_update(request,id):
    notification1=notification.objects.get(id=id)
    form=notificationform(instance=notification1)
    if request.method=="POST":
        form=notificationform(request.POST,instance=notification1)
    if form.is_valid():
        form.save()
        return redirect('view_notification')
    return render(request,'addnotification.html',{'form':form})


@login_required(login_url='log')
def notification_delete(request,id):
    notification.objects.get(id=id).delete()
    return redirect('view_notification')


@login_required(login_url='log')
def attendance_update(request,id):
    attendance1=attendance.objects.get(id=id)
    form=attendanceform(instance=attendance1)
    if request.method=="POST":
        form=attendanceform(request.POST,instance=attendance1)
    if form.is_valid():
        form.save()
        return redirect('view_attendance')
    return render(request,'addattendance.html',{'form':form})


@login_required(login_url='log')
def attendance_delete(request,id):
    attendance.objects.get(id=id).delete()
    return redirect('view_attendance')


@login_required(login_url='log')
def staff_update(request,id):
    staff1=staff.objects.get(id=id)
    form=staffform(instance=staff1)
    if request.method=="POST":
        form=staffform(request.POST,instance=staff1)
    if form.is_valid():
        form.save()
        return redirect('view_staff')
    return render(request,'addstaff.html',{'form':form})


@login_required(login_url='log')
def staff_delete(request,id):
    staff.objects.get(id=id).delete()
    return redirect('view_staff')


@login_required(login_url='log')
def view_complaint(request):
    data = complaint.objects.all()
    return render(request, 'viewcomplaint.html', {'data': data})


@login_required(login_url='log')
def view_booking(request):
    data = booking.objects.all()
    return render(request, 'viewbooking.html', {'data': data})



def approve_booking(request,id):
    booking1=booking.objects.get(id=id)
    booking1.status = 1
    booking1.save()
    messages.info(request,"Booking approved succesfully")
    return redirect('view_booking')

def reject_booking(request,id):
    booking1=booking.objects.get(id=id)
    # if request.method=='POST':
    booking1.status = 2
    booking1.save()
    messages.info(request,"Booking registration rejected")
    return redirect('view_booking')


@login_required(login_url='log')
def view_review(request):
    data = review.objects.all()
    return render(request, 'viewreview.html', {'data': data})

@login_required(login_url='log')
def com_replay(request,id):
    f=complaint.objects.get(id=id)
    if request.method== "POST":
        r=request.POST.get('replay')
        f.replay=r
        f.save()
        return redirect('view_complaint')
    return render(request,'addreplay.html',{'f':f})


def logout_view(request):
    logout(request)
    return redirect('log')
















