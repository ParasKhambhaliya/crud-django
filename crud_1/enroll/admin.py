from django.contrib import admin
from .models import ModelStudent

# Register your models here.
@admin.register(ModelStudent)
class AdminStudent(admin.ModelAdmin):
    list_display = ('id','name' , 'email' , 'password')