from django.contrib import admin
from .models import CricketPlayerT20, CricketPlayerODI, CricketPlayerTest, CricketPlayerIPL


@admin.register(CricketPlayerT20)
class CricketPlayerT20Admin(admin.ModelAdmin):
    list_display = ['id', 'name',]
    list_display_links = ['id', 'name']

@admin.register(CricketPlayerODI)
class CricketPlayerODIAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']

@admin.register(CricketPlayerTest)
class CricketPlayerTestAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']

@admin.register(CricketPlayerIPL)
class CricketPlayerIPLAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    




