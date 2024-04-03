from django.contrib import admin

from apps.models import Sheep


# Register your models here.

@admin.register(Sheep)
class SheepAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'address', 'email', 'phone', 'photo']
