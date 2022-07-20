from django.contrib import admin

# Register your models here.
from .models import Autor, Notes

admin.site.register(Autor)
admin.site.register(Notes)