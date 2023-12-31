from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    ROLE_CHOICES = (
        ("user", "User"),
        ("Steve Jobs", "Steve Jobs"),
    )
    role = models.CharField(max_length=15, choices=ROLE_CHOICES)
    content = models.TextField()
    user = models.ForeignKey(User,null=True, blank=True, on_delete=models.CASCADE)

class Feedback(models.Model):
    RATINGS = (
        ('best', 'Best'),
        ('good', 'Good'),
        ('normal', 'Normal'),
        ('bad', 'Bad'),
        ('worst', 'Worst'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.CharField(max_length=10, choices=RATINGS)

# class Chat(models.Model):
#     userid = models.ForeignKey(User, on_delete=models.CASCADE)
#     message = models.TextField()
#     response = models.TextField()
#     timestamp = models.DateTimeField(auto_now_add=True)
