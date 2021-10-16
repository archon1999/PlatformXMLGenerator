import random
import string

from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


class AdminManager(UserManager):
    def get_queryset(self):
        return super().get_queryset().filter(is_superuser=True)


class User(AbstractUser):
    class Type(models.IntegerChoices):
        USER = 0, 'Пользователь без прав'
        VERIFIED = 1, 'Пользователь'
        ADMIN = 2, 'Администратор'

    users = UserManager()
    admins = AdminManager()
    type = models.IntegerField(default=Type.USER, choices=Type.choices)
    date_of_birth = models.DateField(null=True)
    token = models.CharField(max_length=255, default='')

    def update_token(self):
        token = str()
        for _ in range(20):
            token += random.choice(string.ascii_letters+string.digits)

        self.token = token
        self.save()

    def __str__(self):
        return str(self.username)


class Platform(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True,
        verbose_name='Название',
    )
    created = models.DateTimeField(auto_now_add=True,
                                   verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True,
                                   verbose_name='Дата изменения')

    class Meta:
        verbose_name = 'Платформа'
        verbose_name_plural = 'Платформы'

    def __str__(self):
        return self.name


class Category(models.Model):
    platform = models.ForeignKey(
        to=Platform,
        on_delete=models.CASCADE,
        related_name='categories',
        verbose_name='Платформа',
    )
    name = models.CharField(
        max_length=255,
        unique=True,
        verbose_name='Название',
    )
    parent = models.ForeignKey(
        to='self',
        on_delete=models.CASCADE,
        related_name='children',
        null=True,
        blank=True,
        verbose_name='Родитель',
    )
    xml_feed = models.CharField(max_length=255,
                                verbose_name='Значение для XML фида')
    created = models.DateTimeField(auto_now_add=True,
                                   verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True,
                                   verbose_name='Дата изменения')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name
