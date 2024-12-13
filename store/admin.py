from django.contrib import admin
from .models import Category, Game, Address


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title',)


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'price')
    list_filter = ('category',)
    search_fields = ('title', 'description')


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'country', 'city', 'address')
