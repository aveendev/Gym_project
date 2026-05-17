from django.contrib import admin
from .models import GymnasticsCoach,KarateCoach,GymnasticsPlayer,KaratePlayer
# Register your models here.

@admin.register(GymnasticsCoach)
class GymnasticsCoachAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'phone_number', 'gym']
    search_fields = ['full_name','gym__name']

@admin.register(KarateCoach)
class KarateCoachAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'phone_number', 'gym']
    search_fields = ['full_name','gym__name']

@admin.register(GymnasticsPlayer)
class GymnasticsPlayerAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'phone_number', 'gym']
    search_fields = ['full_name','gym__name']

@admin.register(KaratePlayer)
class KaratePlayerAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'phone_number', 'gym']
    search_fields = ['full_name','gym__name']
    

