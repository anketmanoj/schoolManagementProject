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

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password
        )

        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
