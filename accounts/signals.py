from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.models import User, UserProfile

@receiver(post_save, sender = User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Signal to automatically create a profile when a new user is created.
    """
    if created and not hasattr(instance, 'profile'):
        UserProfile.objects.create(user = instance)
