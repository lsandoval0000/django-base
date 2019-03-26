from django.conf import settings
from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.mail import send_mail


class UserManager(BaseUserManager, models.Manager):
    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
        email = self.normalize_email(email)
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=email, is_active=True, is_staff=is_staff, is_superuser=is_superuser,
                          **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, False, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, True, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('email', max_length=255, unique=True)
    first_name = models.CharField('first name', max_length=255)
    last_name = models.CharField('last name', max_length=255)
    is_active = models.BooleanField('active', default=True)
    is_staff = models.BooleanField('staff', default=False)
    is_superuser = models.BooleanField('superuser', default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    # Aquí coloca los campos que desees agregar
    avatar = models.URLField('avatar', null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)