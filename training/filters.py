from django_filters import rest_framework as filters
from .models import Equipment

class EquipmentFilter(filters.FilterSet):
    name = filters.CharFilter(field_name="name", lookup_expr='icontains')
    min_quantity = filters.NumberFilter(field_name="quantity", lookup_expr='gte')
    max_quantity = filters.NumberFilter(field_name="quantity", lookup_expr='lte')

    class Meta:
        model = Equipment
        fields = ['name', 'quantity'] 
        