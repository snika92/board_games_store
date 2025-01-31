from django.db import models

from users.models import User


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']


class Game(models.Model):
    title = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    image = models.ImageField(upload_to='images/', null=True, blank=True, verbose_name='Изображение')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='games', verbose_name='Категория')
    price = models.FloatField(verbose_name='Цена за покупку')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')
    owner = models.ForeignKey(User, verbose_name="Владелец", help_text="Укажите владельца товара", blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'
        ordering = ['title']
        permissions = [
            ("can_unpublish_product", "Can unpublish product"),
        ]


class Address(models.Model):
    country = models.CharField(max_length=50, verbose_name='Страна')
    city = models.CharField(max_length=50, verbose_name='Город')
    address = models.TextField(verbose_name='Адрес')

    def __str__(self):
        return f'{self.country}, {self.city}, {self.address}'

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'
