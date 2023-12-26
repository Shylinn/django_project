# real_estate_app/admin.py

from django.contrib import admin
from .models import UserProfile, BusinessInfo, Category, Post

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'email', 'role', 'business_title')  # Thêm 'business_title' vào danh sách hiển thị
    search_fields = ('user__username', 'user__email', 'business__title')  # Thêm 'business__title' vào trường tìm kiếm

@admin.register(BusinessInfo)
class BusinessInfoAdmin(admin.ModelAdmin):
    list_display = ('id_business', 'title')
    search_fields = ('title',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'category', 'title', 'status', 'creation_time')
    search_fields = ('user__username', 'title')

