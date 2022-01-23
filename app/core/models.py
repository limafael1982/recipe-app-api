from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):
    """ Manages User model """

    def create_user(self, email, password, **extra_args):
        """ Creates user """
        email_lower = email.lower()
        user = self.model(email=self.normalize_email(email_lower), **extra_args)
        user.set_password(password)
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """ Custom user model """

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=512)
    is_active = models.BooleanField(default=True)
    is_superuser = False
    is_staff = models.BooleanField(default=False)

    objects = UserManager()
    #REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'






