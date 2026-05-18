from django.contrib import admin
from .models import Schedule, Equipment

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ['id', 'day', 'start_time', 'end_time', 'active_coach', 'gym']
    exclude = ['gym']
    list_filter = ['day', 'gymnastics_coach', 'karate_coach', 'start_time', 'gym']
    search_fields = ['active_coach__full_name']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        qs = qs.select_related('gymnastics_coach', 'karate_coach').prefetch_related(
            'gymnastics_players', 'karate_players')
        if request.user.is_superuser:
            return qs
        return qs.filter(gym=request.user.gym)

    def save_model(self, request, obj, form, change):
        if not change and not request.user.is_superuser:
            obj.gym = request.user.gym
        super().save_model(request, obj, form, change)


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'quantity', 'price', 'last_updated', 'gym']
    exclude = ['gym']
    list_filter = ['quantity', 'price', 'last_updated', 'gym']
    search_fields = ['name']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(gym=request.user.gym)

    def save_model(self, request, obj, form, change):
        if not change and not request.user.is_superuser:
            obj.gym = request.user.gym
        super().save_model(request, obj, form, change)