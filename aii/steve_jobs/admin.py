from django.contrib import admin
from .models import Message, Feedback

class MessageAdmin(admin.ModelAdmin):
    list_display = ['user', 'role','content']
    search_fields = ['user']

class FeedbackAdmin(admin.ModelAdmin):
     list_display = ['user','rating']
     search_fields = ['user']

admin.site.register(Message,MessageAdmin)
admin.site.register(Feedback,FeedbackAdmin)
