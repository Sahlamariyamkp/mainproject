from django.contrib import admin

from newprojectapp import models

# Register your models here.
admin.site.register(models.Login_view)
admin.site.register(models.Stud_reg)
admin.site.register(models.Parent_reg)
