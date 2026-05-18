from django.contrib import admin
from .models import Subscription

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ['id', 'start_date', 'price', 'is_paid', 'gym', 'gymnastics_player', 'karate_player']
    exclude = ['gym']
    list_filter = ['is_paid','start_date','gym','gymnastics_player','karate_player']
    search_fields = ['gymnastics_player__full_name','karate_player__full_name']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(gym=request.user.gym)

    def save_model(self, request, obj, form, change):
        if not change:
            if not request.user.is_superuser:
                obj.gym = request.user.gym
        super().save_model(request, obj, form, change)