from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Login_view(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_parent = models.BooleanField(default=False)

class Stud_reg(models.Model):
    user = models.OneToOneField(Login_view,on_delete=models.CASCADE,related_name='student',null=True)
    name = models.CharField(max_length=200)
    reg_id = models.CharField(max_length=25)
    email = models.EmailField()
    phone =models.IntegerField()
    address = models.CharField(max_length=250)
    approval_status = models.IntegerField(default=0)
    student_images = models.ImageField(upload_to="images")

    def __str__(self):
        return self.name
class Parent_reg(models.Model):
    user = models.OneToOneField(Login_view, on_delete=models.CASCADE, primary_key=True,related_name='parent')
    parent_name = models.CharField(max_length=200)
    student_name =  models.ForeignKey(Stud_reg,on_delete=models.CASCADE)
    reg_id = models.CharField(max_length=25)
    email = models.EmailField()
    phone = models.IntegerField()
    address = models.CharField(max_length=250)
    approval_status=models.IntegerField(default=0)

    def __str__(self):
        return self.student_name

class hostel(models.Model):
    hostel_name=models.CharField(max_length=200)
    location=models.CharField(max_length=200)
    room_fecilities=models.CharField(max_length=150)
    contact_number=models.IntegerField()
    hostel_images=models.ImageField(upload_to="images")

    def __str__(self):
        return self.hostel_name

class food(models.Model):
    breakfast=models.CharField(max_length=200)
    lunch=models.CharField(max_length=200)
    eveningsnacks=models.CharField(max_length=200)
    dinner=models.CharField(max_length=200)

    def __str__(self):
        return self.dinner

class fee(models.Model):
    hostelname= models.ForeignKey(hostel,on_delete=models.CASCADE)
    room_rent =models.FloatField(default=0)
    mess_bill =models.FloatField(default=0)
    amount =models.FloatField(default=0)

    def __str__(self):
        return self.amount


class payment(models.Model):
    studentname = models.ForeignKey(Stud_reg,on_delete=models.CASCADE)
    room_rent = models.IntegerField(default=0)
    mess_bill = models.IntegerField(default=0)
    from_date = models.DateField()
    to_date = models.DateField()
    amount = models.IntegerField(default=0)
    status =  models.IntegerField(default=0)

    def __str__(self):
        return self.studentname


class notification(models.Model):
    date= models.DateField()
    add_message = models.CharField(max_length=200)



    def __str__(self):
        return self.name



class attendance(models.Model):
    user= models.ForeignKey(Stud_reg,on_delete=models.CASCADE)
    status = models.CharField(max_length=200)




    def __str__(self):
        return self.status

class staff(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    contactnumber = models.IntegerField()


    def __str__(self):
        return self.name

class complaint(models.Model):
    user=models.ForeignKey(Login_view,on_delete=models.DO_NOTHING)
    date=models.DateField()
    complaint=models.TextField(max_length=2000)
    replay=models.TextField(null=True,blank=True)

    def __str__(self):
        return self.name

class booking(models.Model):
    name= models.ForeignKey(Stud_reg,on_delete=models.CASCADE)
    date_joining=models.DateField()
    booking_date=models.DateField()
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class review(models.Model):
    name=models.ForeignKey(Stud_reg,on_delete=models.DO_NOTHING)
    date=models.DateField()
    review=models.TextField(max_length=2000)

    def __str__(self):
        return self.name








