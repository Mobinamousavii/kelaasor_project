# from django.db.models.signals import post_save, post_migrate
# from django.dispatch import receiver
# from django.contrib.auth.models import Group, Permission
# from accounts.models import User

# @receiver(post_migrate)
# def setup_groups(sender, **kwargs):
#     groups = [
#         'Students',
#         'Teachers',
#         'Support_Team',
#         'Financial_Team',
#         'Content_Team',
#         'superusers'
#     ]

#     for group_name in groups:
#         Group.objects.get_or_create(name = group_name)

    