from django.contrib import admin
from .models import *
from django import forms

admin.site.register(Businessinfo)
admin.site.register(Category)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'category']
    search_fields  = ['user']
admin.site.register(Post,PostAdmin)
