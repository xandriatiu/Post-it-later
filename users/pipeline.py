import logging

from django.contrib.auth.models import User
from django.core.exceptions import (
    ObjectDoesNotExist,
    MultipleObjectsReturned
)

from queue.models import Bots
from users.models import UserProfile

logger = logging.getLogger(__name__)

def save_profile(backend, user, response, *args, **kwargs):
    try:
        get_user = User.objects.get(id=user.id)
    except (ObjectDoesNotExist, MultipleObjectsReturned) as e:
        logger.error('Error: {e}'.format(e=e))

    profile, created = UserProfile.objects.get_or_create(user=get_user)

    if created:
        profile.bots.add(Bots.objects.all()[0])
    profile.save()