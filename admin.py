from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Student)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id' ,'name', 'email',  'password', 'status')


@admin.register(Attend)
class AttendAdmin(admin.ModelAdmin):
    list_display = ('id' ,'name', 'email',  'password', 'status')
