from django.contrib import admin

# Register your models here.
from .models import Comment, TestModel

admin.site.register(Comment)
admin.site.register(TestModel)