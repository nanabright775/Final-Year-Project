from django import template
from django.db.models import Model
from django.contrib.contenttypes.models import ContentType
from ..models import Like, Comment

register = template.Library()

@register.filter
def model_name(value):
    if isinstance(value, Model):
        return value._meta.model_name
    return ''

    return Comment.objects.filter(content_type=content_type, object_id=item.id).count()

@register.simple_tag
def get_content_type_id(instance):
    content_type = ContentType.objects.get_for_model(instance)
    return content_type.id