from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from django.db import models
from .forms import SignupForm
from .models import User


class UsersFormLayout(UserAdmin):
    model = User
    add_form = SignupForm
    list_display = ['username', 'gender']
    readonly_fields = ['gender', 'phone_no', 'profile_pic']
    

admin.site.register(User, UsersFormLayout)