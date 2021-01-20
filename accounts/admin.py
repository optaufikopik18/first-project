from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from .forms import CustomUserCreationFrom, CustomUserChangeForm

# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationFrom
    form = CustomUserChangeForm
    model = User
    list_display = ('username','email','date_of_birth','gender','is_active')
    fieldsets = (
        (None, {
            'fields': (
                'first_name',
                'last_name',
                'username',
                'email',
                'date_of_birth',
                'gender',
                'is_active'
            ),
        }),
    )
    add_fieldsets = (
        (None, {
            'fields': (
                'first_name',
                'last_name',
                'username',
                'email',
                'password1',
                'password2',
                'date_of_birth',
                'gender'
            ),
        }),
    )

admin.site.register(User,CustomUserAdmin)
