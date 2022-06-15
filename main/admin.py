from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Monk

class MonkAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('user_name', 'userpic', 'first_name', 'city_of_origin', 'title', 'is_literate', 'is_ordained', 'about')}),
        ('Permissions', {'fields': (
            'is_active', 
            'is_staff', 
            'is_superuser',
            'groups', 
            'user_permissions',
        )}),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('user_name', 'password1', 'password2')
            }
        ),
    )

    list_display = ('user_name', 'title', 'first_name', 'city_of_origin', 'is_staff', 'is_superuser', 'last_login', 'start_date')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('user_name',)
    ordering = ('user_name',)
    filter_horizontal = ('groups', 'user_permissions',)

admin.site.register(Monk, MonkAdmin)

