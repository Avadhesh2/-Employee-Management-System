from django.contrib import admin
from .models import Employee, Department  # Role,
# Register your models here.
# regirter all models in admin.py
# It helps to get all these in admin portal
admin.site.register(Employee)
# admin.site.register(Role)
admin.site.register(Department)
