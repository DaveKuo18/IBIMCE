from django.contrib import admin

from .models import reuniones_comunes, reuniones_especiales

# Register your models here.
admin.site.register(reuniones_comunes)
admin.site.register(reuniones_especiales)