from django.dispatch import receiver
from django.db.models.signals import m2m_changed
from django.contrib.auth import get_user_model
from notifications.utils import create_notification

User = get_user_model()

@receiver(m2m_changed, sender=User.following.through)
def notify_on_follow(sender, instance, action, reverse, pk_set, **kwargs):
    # instance follows users whose pks are in pk_set
    if action == "post_add" and pk_set:
        for pk in pk_set:
            try:
                target = User.objects.get(pk=pk)
                create_notification(
                    recipient=target,
                    actor=instance,
                    verb="started following you",
                    target_obj=instance,  # actor as target for simple text
                )
            except User.DoesNotExist:
                pass
