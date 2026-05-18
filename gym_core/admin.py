from django.contrib import admin
from .models import GymnasticsCoach,KarateCoach,GymnasticsPlayer,KaratePlayer
# Register your models here.

@admin.register(GymnasticsCoach)
class GymnasticsCoachAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'phone_number', 'gym']
    search_fields = ['full_name', 'gym__name']
    list_filter = ['gym']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(gym=request.user.gym)

    def save_model(self, request, obj, form, change):
        if not change and not request.user.is_superuser:
            obj.gym = request.user.gym
        super().save_model(request, obj, form, change)


@admin.register(KarateCoach)
class KarateCoachAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'phone_number', 'gym']
    search_fields = ['full_name', 'gym__name']

    list_filter = ['gym']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(gym=request.user.gym)

    def save_model(self, request, obj, form, change):
        if not change and not request.user.is_superuser:
            obj.gym = request.user.gym
        super().save_model(request, obj, form, change)

@admin.register(GymnasticsPlayer)
class GymnasticsPlayerAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'phone_number', 'gym']
    search_fields = ['full_name', 'gym__name']

    list_filter = ['gym']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(gym=request.user.gym)

    def save_model(self, request, obj, form, change):
        if not change and not request.user.is_superuser:
            obj.gym = request.user.gym
        super().save_model(request, obj, form, change)


@admin.register(KaratePlayer)
class KaratePlayerAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'phone_number', 'gym']
    search_fields = ['full_name', 'gym__name']

    list_filter = ['gym']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(gym=request.user.gym)

    def save_model(self, request, obj, form, change):
        if not change and not request.user.is_superuser:
            obj.gym = request.user.gym
        super().save_model(request, obj, form, change)

