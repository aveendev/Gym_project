from django.urls import path
from . import views

urlpatterns = [
    path('schedules/', views.ScheduleListCreateView.as_view(), name='schedule-list-create'),
    path('schedule/<int:pk>/', views.ScheduleDetailView.as_view(), name='schedule-detail'),
    path('equipments/', views.EquipmentList.as_view(), name='equipment-list'),
    path('equipment/<int:pk>/', views.EquipmentDetail.as_view(), name='equipment-detail'),
    path('public/equipments/', views.PublicEquipmentList.as_view(), name='public-equipment-list'),
]
