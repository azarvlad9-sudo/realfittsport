from django.contrib import admin
from .models import Client, Trainer

@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialization')

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    # Ми прибрали created_at, бо його немає в моделі.
    # Додали відображення тренера та типу абонемента.
    list_display = ('full_name', 'phone', 'sub_type', 'trainer', 'is_active')
    list_filter = ('is_active', 'sub_type', 'trainer')
    search_fields = ('full_name', 'phone')