from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import GymnasticsPlayerViewSet,KaratePlayerViewSet, GymnasticsCoachViewSet,KarateCoachViewSet


router = DefaultRouter()
router.register(r'gymnastics_players',GymnasticsPlayerViewSet,basename='gymnastics_players')
router.register(r'karate_players',KaratePlayerViewSet,basename='karate_players')
router.register(r'gymnastics_coaches', GymnasticsCoachViewSet,basename='gymnastics_coaches')
router.register(r'karate_coaches', KarateCoachViewSet,basename='karate_coaches')


urlpatterns = [
    path('', include(router.urls))
]