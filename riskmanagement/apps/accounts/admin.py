from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
    # The forms to add and change user instances
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    model = CustomUser

    list_display = ('email','username','first_name', 'last_name','date_joined', 'last_login', 'is_admin','is_staff','is_superuser', 'is_active',)
    search_fields = ('first_name', 'last_name','email','username')
    readonly_fields=('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
 
admin.site.register(CustomUser, CustomUserAdmin)