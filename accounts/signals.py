from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from django.contrib.auth import get_user_model


@receiver(post_save, sender=get_user_model())
def create_auth_token(sender, instance=None, created=False, **kwargs):
    """
    Creates an authentication token for a CustomUser instance after it is saved.

    Args:
        sender: The sender of the signal.
        instance: The CustomUser instance that was saved.
        created: A boolean indicating if the instance was created or updated.

    Raises:
        None.

    Returns:
        None.
    """
    if created:
        Token.objects.create(user=instance)
