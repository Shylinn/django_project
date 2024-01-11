# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
import requests
from django.urls import reverse
from django.contrib.auth.models import User






class Businessinfo(models.Model):
    id_business = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    def __str__(self):
        return self.title

    class Meta:
        managed = False
        db_table = 'BusinessInfo'
class Tinh(models.Model):
    ten_tinh = models.CharField(primary_key=True, max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')

    class Meta:
        managed = False
        db_table = 'tinh'
    def __str__(self):
        return self.ten_tinh


class Category(models.Model):
    name = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    def __str__(self):
        return self.name
    class Meta:
        managed = False
        db_table = 'Category'

class Huyen(models.Model):
    ten_huyen = models.CharField(primary_key=True, max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    ten_tinh = models.ForeignKey('Tinh', models.DO_NOTHING, db_column='ten_tinh', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'huyen'
    def __str__(self):
        return self.ten_huyen



class Post(models.Model):
    REGION_CHOICES = [
        ('Đông', 'Đông'),
        ('Tây', 'Tây'),
        ('Nam', 'Nam'),
        ('Bắc', 'Bắc'),
    ]
    # user = models.ForeignKey('Userprofile', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,editable=False)
    # user_name = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    user_name = models.CharField(max_length=100, editable=False)

    category = models.ForeignKey(Category, models.DO_NOTHING, blank=True, null=True)
    title = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    body = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    image_url = models.ImageField(upload_to='images/')
    province = models.ForeignKey('Tinh', models.DO_NOTHING, db_column='province', blank=True, null=True)
    district = models.ForeignKey('Huyen', models.DO_NOTHING, db_column='district', blank=True, null=True)
    price = models.FloatField(blank=True, null=True, default=0)
    # creation_time = models.DateTimeField(blank=True, null=True)
    # published_time = models.DateTimeField(blank=True, null=True)
    # status = models.CharField(max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    area = models.FloatField(blank=True, null=True)
    bedroom = models.IntegerField(blank=True, null=True)
    toilet = models.IntegerField(blank=True, null=True)
    furniture = models.IntegerField(blank=True, null=True)
    facade = models.IntegerField(blank=True, null=True)
    house_direction = models.CharField(
        max_length=10,
        choices=REGION_CHOICES,
        default='Đông'
        
    )
    way = models.FloatField(blank=True, null=True)
    pacony_direction = models.CharField(
        max_length=10,
        choices=REGION_CHOICES,
        default='Đông'
        
    )
    floor = models.IntegerField(blank=True, null=True)

    def save(self, *args, **kwargs):
        # Gán giá trị user_name và user_id trước khi lưu
        self.user_name = self.user.username
        self.user_id = self.user.id
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    class Meta:
        managed = False
        db_table = 'Post'
   


# class Userprofile(models.Model):
#     id_user = models.AutoField(primary_key=True)
#     username = models.CharField(unique=True, max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
#     password = models.CharField(max_length=128, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
#     email = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
#     phone = models.CharField(max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
#     profile_image = models.ImageField(upload_to='media/images/profile')
#     role_id = models.CharField(max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
#     business = models.ForeignKey(Businessinfo, models.DO_NOTHING, blank=True, null=True)
#     def __str__(self):
#         return self.username
#     class Meta:
#         managed = False
#         db_table = 'UserProfile'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS')

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128, db_collation='SQL_Latin1_General_CP1_CI_AS')
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS')
    first_name = models.CharField(max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS')
    last_name = models.CharField(max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS')
    email = models.CharField(max_length=254, db_collation='SQL_Latin1_General_CP1_CI_AS')
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    object_repr = models.CharField(max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS')
    action_flag = models.SmallIntegerField()
    change_message = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS')
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    model = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    name = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS')
    session_data = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS')
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'

