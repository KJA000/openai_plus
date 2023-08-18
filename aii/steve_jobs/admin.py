from django.contrib import admin
from .models import Message

class MessageAdmin(admin.ModelAdmin):
    list_display = ['user', 'role','content']
    search_fields = ['user']

admin.site.register(Message,MessageAdmin)
    
