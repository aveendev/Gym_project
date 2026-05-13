from django.urls import path
from . import views

urlpatterns = [
    path('subscriptions/', views.SubscriptionListCreateView.as_view(), name='subscription-list'),
    path('subscription/<int:pk>/', views.SubscriptionDetailView.as_view(), name='subscription-detail'),
]
