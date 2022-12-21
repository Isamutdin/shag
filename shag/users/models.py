from django.db import models
from .managers import CustomUserManager
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
# Create your models here.

class CustomUser(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(_('username'), max_length=30, unique=True, null=True, blank=True)
    email = models.EmailField(_('email'), max_length=40, unique=True)
    phone = models.CharField(_('phone'), max_length=30, unique=True, null=True, blank=True)

    name = models.CharField(_('Имя'), max_length=30, null=True, blank=True)
    second_name = models.CharField(_('Фамилия'), max_length=30, null=True, blank=True)
    date_create = models.DateTimeField(_('Дата создания'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('staff'), default=False)

    STATUS_CHOICES = [
    ('TC', 'Учитель'),
    ('ST', 'Ученик'),
    ('A', 'Администратор'),
    ('SR', 'Представитель школы'),
    ('R', 'Резерв'),
    ]

    status = models.CharField(
        max_length=2,
        choices=STATUS_CHOICES,
        default='ST',
        null=True,
    )

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = CustomUserManager()

    def __str__(self):
        return str(self.email)

    class Meta:
        unique_together = ('username', 'email', 'phone')
