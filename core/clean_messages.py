import os
import django

# Налаштуйте Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from sim.models import Message,Chat

def clean_invalid_messages():
    invalid_messages = Message.objects.exclude(chat_id__in=Chat.objects.values_list('id', flat=True))
    invalid_messages.delete()

if __name__ == "__main__":
    clean_invalid_messages()
