from django.contrib import admin
from .models import Conversations, ConversationMessage

admin.site.register(Conversations)
admin.site.register(ConversationMessage)
