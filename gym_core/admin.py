from django.contrib import admin
from .models import GymnasticsCoach,KarateCoach,GymnasticsPlayer,KaratePlayer
# Register your models here.

admin.site.register(GymnasticsCoach)
admin.site.register(KarateCoach)
admin.site.register(GymnasticsPlayer)
admin.site.register(KaratePlayer)

