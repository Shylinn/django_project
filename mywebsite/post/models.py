# real_estate_app/models.py

from django.db import models
from django.contrib.auth.models import User, Group
from django.utils import timezone

class BusinessInfo(models.Model):
    id_business = models.AutoField(primary_key=True,default=1),
    title = models.CharField(max_length=255)
    # Các thuộc tính khác của BusinessInfo

class UserProfile(models.Model):
    id_user = models.AutoField(primary_key=True,default=1)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    profile_image = models.URLField()
    role = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True)
    business = models.OneToOneField(BusinessInfo, on_delete=models.SET_NULL, null=True, blank=True)

    @property
    def business_title(self):
        return self.business.title if self.business else None

    @property
    def username(self):
        return self.user.username

class Category(models.Model):
    name = models.CharField(max_length=255)

class Post(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('active', 'Active'),
    ]

    DIRECTION_CHOICES = [
        ('east', 'Đông'),
        ('west', 'Tây'),
        ('south', 'Nam'),
        ('north', 'Bắc'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = models.TextField()
    image_url = models.URLField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    creation_time = models.DateTimeField(auto_now_add=True)
    published_time = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    area = models.FloatField()
    bedroom = models.PositiveIntegerField()
    toilet = models.PositiveIntegerField()
    furniture = models.BooleanField()
    facade = models.BooleanField()
    house_direction = models.CharField(max_length=50, choices=DIRECTION_CHOICES)
    way = models.FloatField()
    pacony_direction = models.CharField(max_length=50, choices=DIRECTION_CHOICES)
    floor = models.PositiveIntegerField()
