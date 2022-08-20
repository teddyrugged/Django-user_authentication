from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

# Create your models here.


class ProfileManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError("The Email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault("is_admin", True)
        extra_fields.setdefault("is_staff", True)
        if extra_fields.get("is_admin") is not True:
            raise ValueError("user must have is_admin=True.")
        if extra_fields.get("is_staff") is not True:
            raise ValueError("user must have is_staff=True.")
        user =self.create_user(email, password, **extra_fields)
        return user
    


class Profile(AbstractBaseUser):
    email = models.EmailField(verbose_name='email address',max_length=60, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    confirm_password = models.CharField(max_length=255)
    is_staff = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True) 
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS =['first_name', 'last_name']
    
    objects = ProfileManager()
    
    
    def __str__(self):
        return self.last_name
    