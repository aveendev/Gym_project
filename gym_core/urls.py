from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import GymnasticsPlayerViewSet,KaratePlayerViewSet, GymnasticsCoachViewSet,KarateCoachViewSet


router = DefaultRouter()
router.register(r'gymnastics_players',GymnasticsPlayerViewSet)
router.register(r'karate_players',KaratePlayerViewSet)
router.register(r'gymnastics_coaches', GymnasticsCoachViewSet)
router.register(r'karate_coaches', KarateCoachViewSet)


urlpatterns = [
    path('', include(router.urls))
]