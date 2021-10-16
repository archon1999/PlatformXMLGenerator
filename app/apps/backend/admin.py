from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from apps.backend.models import User, Platform, Category

admin.site.register(User, UserAdmin)


@admin.register(Platform)
class PlatformAdmin(admin.ModelAdmin):
    list_display = ['name', 'created', 'updated']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['platform', 'name', 'parent', 'xml_feed',
                    'created', 'updated']
