from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Employee


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['firstname', 'middlename', 'lastname', 'position', 'joined_date', 'salary', 'supervisor']
    search_fields = ['firstname', 'middlename', 'lastname', 'position', 'joined_date', 'salary']

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Employee, EmployeeAdmin)
