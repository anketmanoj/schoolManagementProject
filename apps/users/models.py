from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)

# create a custom user manager that inherits from BaseUserManager to create user and superuser


class CustomUserManager(BaseUserManager):
    # method to create user
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    # create method for creating superuser

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password
        )

        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    is_student = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "All the users have all the permissions"
        return True

    def has_module_perms(self, app_label):
        "All users have permissions to view the app"
        return True


class UserProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    preferred_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='profile-image')
    discord_name = models.CharField(max_length=100)
    github_username = models.CharField(max_length=100)
    codepen_username = models.CharField(max_length=100)
    fcc_profile_url = models.URLField(max_length=255)

    LEVELS = (
        (1, 'Beginner'),
        (2, 'Intermediate'),
        (3, 'Advanced'),
        (4, 'Expert'),
        (5, 'Master'),
        (6, 'Grandmaster'),
        (7, 'Challenger'),
        (8, 'Legendary'),
    )

    current_level = models.IntegerField(choices=LEVELS, default="Beginner")
    phone = models.CharField(max_length=20)
    timezone = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name + " " + self.last_name
