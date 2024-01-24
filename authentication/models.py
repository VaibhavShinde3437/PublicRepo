from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from rest_framework_simplejwt.tokens import RefreshToken

class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError(('Users must have an email address'))
        if not username:
            raise ValueError(('Users must have an username'))
       
        email = self.normalize_email(email)
        user = self.model(email=email,username=username, password=password)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email,username, password=None):
        if not password is None:
            raise ValueError(('Enter a password'))
        user = self.create_user(email,username, password)
        user.is_superuser = True
        user.is_staff=True
        user.save()
        return user

    
class User(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20, unique=True, db_index=True)
    email = models.EmailField(max_length =50, unique=True, db_index=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
 

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.username
    
    def tokens(user):
        return {
            "refresh" : str(RefreshToken.for_user(user)),
            "access" : str(RefreshToken.for_user(user).access_token)
    }

class Assessment(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

        
    def __str__(self):
        return self.title
    
class Question(models.Model):
    CHOICES= [
        ('text', 'Free Text'),
        ('single_select', 'Single Select'),
        ('multi_select', 'Multi Select'),
        ('rating', 'Rating'),
    ]

    assessment = models.ForeignKey(to=Assessment, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    options = models.JSONField(default=list)
    question_type = models.CharField(max_length=20, choices=CHOICES)
    description = models.TextField()

    def __str__(self):
        return self.title


