from django.db import models

class User(models.Model):
    username = models.CharField(max_length=255)
    password_hash = models.CharField(max_length=255)
    email = models.EmailField()
