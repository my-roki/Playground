from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=10)
    password = models.CharField(blank=False, max_length=20)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    group = models.IntegerField()
    is_active = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["created_at"]
