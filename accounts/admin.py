from django.contrib import admin

from .models import UserAccount


@admin.register(UserAccount)
class CallRequestAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'created', 'updated', 'name', 'balance', 'chat_id']
    search_fields = ['user', 'created', 'updated', 'name', 'balance', 'chat_id']
    ordering = ['id']

