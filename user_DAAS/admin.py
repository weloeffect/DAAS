from django.contrib import admin
from .models import DAAS_User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.


class MyAdmin(BaseUserAdmin):
    list_display = ('first_name', 'email', 'last_name', 'phone_number')
    search_fields = ('phone_number', 'first_name')
    # readonly_fields = ('last_login', '')
    filter_horizontal = ()
    list_filter = ('phone_number', 'last_name')
    fieldsets = ()
    add_fieldsets = (
        (None, {
            'classes': ('wide'),
            'fields': ('email', 'first_name', 'last_name', 'phone_number')
        }),
    )
    ordering = ('email', )

admin.site.register(DAAS_User, MyAdmin)