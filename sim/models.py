# models.py
from django import forms
from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=500)

class Chat(models.Model):
    chat_name = models.CharField(max_length=100)
    participants = models.CharField(max_length=1000)
    password = models.CharField(max_length=50)  # Додано поле для пароля чату

class Message(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    chat_id = models.CharField(max_length=255)






    