from django.urls import path
from .views import *

urlpatterns = [
    path('quote/featured/', FeaturedQuoteAPIView.as_view(), name='featured-quote'),
    path('quotes/', AdminQuoteListCreateAPIView.as_view(), name='admin-quote-list-create'),
    path('quotes/<int:pk>/', AdminQuoteDetailAPIView.as_view(), name='admin-quote-detail'),
]