from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User


class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password', 'last_name', 'first_name')}),
        ('Permissions', {'fields': (
            'is_active',
            'is_staff', 
            'is_superuser',
        )}),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('email', 'password1', 'password2')
            }
        ),
    )

    list_display = ('email', 'last_name', 'first_name', 'is_staff')
    list_filter = ('is_superuser', 'is_active')
    search_fields = ('email',)
    ordering = ('email',)
    #filter_horizontal = ('groups', 'user_permissions',)


admin.site.register(User, UserAdmin)