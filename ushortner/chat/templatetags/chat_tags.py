from django import template
from chat.models import Message

register = template.Library()

@register.simple_tag
def unread_message_count(user):
    return Message.objects.filter(receiver=user, is_read=False).count()
