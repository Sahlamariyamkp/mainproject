import datetime

import re

from django import forms

from django.contrib.auth.forms import UserCreationForm

from django.core.exceptions import ValidationError

from django.core.validators import  RegexValidator

from newprojectapp.models import Stud_reg, Parent_reg, Login_view,hostel,food,fee,payment,notification,attendance,staff,complaint,booking,review


class DateInput(forms.DateInput):
    input_type="date"

def phone_number_validator(value):
    if not re.compile(r'^[7-9]\d{9}$').match(value):
        raise ValidationError('This is Not a Valid Phone Number')


class loginregister(UserCreationForm):
    class Meta:
        model= Login_view
        fields=('username','password1','password2',)

class studentform(forms.ModelForm):
    phone=forms.CharField(validators=[phone_number_validator])
    email=forms.CharField(validators=[RegexValidator(regex='^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$',message='Please Enter a Valid Email')])
    class Meta:
        model = Stud_reg
        fields = "__all__"
        exclude = ("user","approval_status",)
    def clean_email(self):
        mail = self.cleaned_data["email"]
        parent_email= Parent_reg.objects.filter(email=mail)
        stud_email=Stud_reg.objects.filter(email=mail)
        if parent_email.exists():
            raise forms.ValidationError("This email already registerd")
        if stud_email.exists():
            raise forms.ValidationError("This email already registerd")
        return mail


    def clean_phone(self):
        phone_no = self.cleaned_data["phone"]
        parent_phone_num= Parent_reg.objects.filter(phone=phone_no)
        stud_phone_num=Stud_reg.objects.filter(phone=phone_no)
        if parent_phone_num.exists():
            raise forms.ValidationError("This phone number already exist")
        if stud_phone_num.exists():
            raise forms.ValidationError("This phone number already exist")
        return phone_no


class parentform(forms.ModelForm):
    phone = forms.CharField(validators=[phone_number_validator])
    email = forms.CharField(validators=[
        RegexValidator(regex='^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$', message='Please Enter a Valid Email')])
    class Meta:
        model = Parent_reg
        exclude = ("user","approval_status",)

    def clean_email(self):
        mail = self.cleaned_data["email"]
        parent_email= Parent_reg.objects.filter(email=mail)
        stud_email=Stud_reg.objects.filter(email=mail)
        if parent_email.exists():
            raise forms.ValidationError("This email already registerd")
        if stud_email.exists():
            raise forms.ValidationError("This email already registerd")
        return mail


    def clean_phone(self):
        phone_no = self.cleaned_data["phone"]
        parent_phone_num= Parent_reg.objects.filter(phone=phone_no)
        stud_phone_num=Stud_reg.objects.filter(phone=phone_no)
        if parent_phone_num.exists():
            raise forms.ValidationError("This phone number already exist")
        if stud_phone_num.exists():
            raise forms.ValidationError("This phone number already exist")
        return phone_no

class hostelform(forms.ModelForm):
    contact_number = forms.CharField(validators=[phone_number_validator])
    class Meta:
        model = hostel
        fields = "__all__"

class foodform(forms.ModelForm):
    class Meta:
        model= food
        fields = "__all__"



class notificationform(forms.ModelForm):
    date=forms.DateField(widget=DateInput)
    class Meta:
        model = notification
        fields ="__all__"

att_choice=(
    ('present','present'),
    ('absent','absent')
)
class attendanceform(forms.ModelForm):
    status=forms.ChoiceField(choices=att_choice,widget=forms.RadioSelect)
    class Meta:
        model = attendance
        fields ="__all__"


class staffform(forms.ModelForm):
    contactnumber = forms.CharField(validators=[phone_number_validator])
    class Meta:
        model = staff
        fields ="__all__"

class complaintform(forms.ModelForm):
    date = forms.DateField(widget=DateInput)
    class Meta:
        model = complaint
        fields ="__all__"
        exclude = ('replay','user',)

    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get("date")
        if date != datetime.date.today():
            raise forms.ValidationError("invalid date")


class replayform(forms.ModelForm):
    class Meta:
        model = complaint
        fields ="__all__"
        exclude = ('user','date','complaint',)


class bookingform(forms.ModelForm):
    date_joining=forms.DateField(widget=DateInput)
    booking_date=forms.DateField(widget=DateInput)
    class Meta:
        model = booking
        fields ="__all__"
        exclude = ('status',)


    def clean(self):
        cleaned_data = super().clean()
        booking_date= cleaned_data.get("booking_date")
        date_joining = cleaned_data.get("date_joining")
        if booking_date != datetime.date.today():
            raise forms.ValidationError("booking_date must be today")
        if date_joining < booking_date :
            raise forms.ValidationError("date_joining must be graterthan booking_date")

class reviewform(forms.ModelForm):
    date = forms.DateField(widget=DateInput)
    class Meta:
        model = review
        fields ="__all__"

    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get("date")
        if date != datetime.date.today():
            raise forms.ValidationError("invalid date")


class feeform(forms.ModelForm):
    date = forms.DateField(widget=DateInput)
    class Meta:
        model = fee
        fields = "__all__"
        exclude =('status',)



class paymentform(forms.ModelForm):
    from_date = forms.DateField(widget=DateInput)
    to_date = forms.DateField(widget=DateInput)
    class Meta:
        model = payment
        fields ="__all__"
        exclude = ('status',)

    def clean(self):
        cleaned_data = super().clean()
        from_date = cleaned_data.get("from_date")
        to_date = cleaned_data.get("to_date")
        if to_date < from_date:
            raise forms.ValidationError("to_date should be greater than from_date.")

