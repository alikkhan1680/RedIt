from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject']
    list_display_links = ['name', 'email', 'subject']
    list_filter = ['name', 'subject']
    search_fields = ['name']

@admin.register(BlogModel)
class BlogModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'created']
    list_display_links = ['title', 'user', 'created']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['cat_name']
    list_display_links = ['cat_name']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['tag']
    list_display_links = ['tag']

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username']
    list_display_links = ['username']

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['user','blog','message']
    list_display_links = ['user','blog','message']


