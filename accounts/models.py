from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, Group, Permission
from django.utils.translation import gettext_lazy as _
# Create your models here.
from .managers import UserManager
# from cloudinary.models import CloudinaryField

class CustomUser(AbstractBaseUser, PermissionsMixin):
    objects = UserManager()
    username = models.CharField(max_length=50, unique=True, blank=True, null=True)
    email = models.EmailField(_('email address'), max_length=300, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    last_login = models.DateTimeField(null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    groups = models.ManyToManyField(
        Group,
        related_name='accounts_user_groups',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name=_('groups'),
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='accounts_user_permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name=_('user permissions'),
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "username"]

    

    def __str__(self):
        return self.email

    @property
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def tokens(self):
        pass


class Attendee(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='attendee')
    phone_number = models.CharField(max_length=15, blank=True, null=True)  # Changed to CharField for better format

    def __str__(self):
        return self.user.email


class Organizer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='organizer')
    org_name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.org_name or self.user.email
    
