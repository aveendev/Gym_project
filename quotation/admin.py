from django.contrib import admin
from .models import Quote

@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'maxim', 'is_featured')
    list_editable = ('is_featured',)