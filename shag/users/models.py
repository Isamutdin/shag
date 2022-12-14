from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    # 'third_name', 'first_name', 'second_name', 'status'
    username = None
    first_name = models.CharField(_('Имя'), max_length=30, null=True,)
    second_name = models.CharField(_('Фамилия'), max_length=30, null=True,)
    third_name = models.CharField(_('Отчество'), max_length=30, null=True,)

    email = models.EmailField(_('Адрес электронной почты'), unique=True)
    school = models.CharField(_('Школа'), max_length=30, null=True,)
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
        default='TC',
        null=True,
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = CustomUserManager()

    def __str__(self):
        return self.email