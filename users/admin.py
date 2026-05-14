from django.contrib import admin
from .models import User

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username','full_name','email','is_staff')
    fields = ['username','full_name','email','is_staff','is_active']
