from django.db import models
from django.contrib.auth.models import User


class Item(models.Model):
    STATUS_CHOICES = [
        ('Lost', 'Lost'),
        ('Found', 'Found'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    date = models.DateField()
    image = models.ImageField(upload_to='items/', blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title