from django.contrib import admin
from .models import Author, Message, Chat

# Реєстрація моделі Author
admin.site.register(Author)
admin.site.register(Message)
admin.site.register(Chat)