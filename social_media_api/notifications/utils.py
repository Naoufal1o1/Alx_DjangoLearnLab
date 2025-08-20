from .models import Notification
from django.contrib.contenttypes.models import ContentType

def create_notification(recipient, actor, verb, target_obj=None):
    ct = None
    obj_id = None
    if target_obj is not None:
        ct = ContentType.objects.get_for_model(target_obj.__class__)
        obj_id = target_obj.id
    return Notification.objects.create(
        recipient=recipient,
        actor=actor,
        verb=verb,
        target_content_type=ct,
        target_object_id=obj_id,
    )
