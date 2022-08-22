from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

# Create your models here.


class ProfileManager(BaseUserManager):
    
    def create_superuser(self, email, password, **other_fields):

      
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')
        if other_fields.get('is_staff') is not True:
            raise ValueError(
            'Superuser must be assigned to is_staff=True.')

        return self.create_user(email, password, **other_fields)

    def create_user(self, email, password, **other_fields):

        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email,
                           **other_fields)
        user.set_password(password)
        user.save()
        return user


class Profile(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"),max_length=60, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(verbose_name='date joined',auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login',auto_now=True)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS =[]
    
    objects = ProfileManager()
    
    
    def __str__(self):
        return self.email
    