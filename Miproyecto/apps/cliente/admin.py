from django.contrib import admin

# Register your models here.
from .models import cliente,pais
admin.site.register(cliente)
admin.site.register(pais)