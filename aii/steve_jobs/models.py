from django.db import models

class Message(models.Model):
    ROLE_CHOICES = (
        ("user", "User"),
        ("Steve Jobs", "Steve Jobs"),
    )
    role = models.CharField(max_length=15, choices=ROLE_CHOICES)
    content = models.TextField()

class Chat(models.Model):
    user_message = models.TextField()
    ai_response = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
