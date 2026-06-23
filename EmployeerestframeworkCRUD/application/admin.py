from django.contrib import admin
from .models import employess

class employeeAdmin(admin.ModelAdmin):
    list_display = ['eid','ename','esal','company','desi']
admin.site.register(employess,employeeAdmin)
