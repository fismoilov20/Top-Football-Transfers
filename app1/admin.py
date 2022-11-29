from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import *

# Register your models here.

@admin.register(Club)
class ClubAdmin(ModelAdmin):
    search_fields = ('name', 'country')
    list_display = ('id', 'name', 'logo', 'country')
    list_display_links = ('name',)

@admin.register(Player)
class PlayerAdmin(ModelAdmin):
    search_fields = ('name', 'club')
    list_display = ('id', 'name', 'club', 'age', 'transfer_value')
    list_display_links = ('name',)

@admin.register(Transfer)
class TransferAdmin(ModelAdmin):
    list_display = ('id', 'player', 'from_club','to_club','season')
    list_display_links = ('player',)
    list_editable= ('season',)