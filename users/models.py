from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):

    USER_CHOICE = [
        ('seeker', 'Seeker'),
        ('listener', 'Listener')
    ]

    name = models.CharField(_("Name"), max_length=100)
    email = models.EmailField(_("Email Address"), max_length=254, unique=True)
    userType = models.CharField(_("User Type"),
                                max_length=10, choices=USER_CHOICE, default='seeker')
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name", "userType"]

    objects = CustomUserManager()

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return self.email

    @property
    def get_full_name(self):
        return f"{self.name}"
