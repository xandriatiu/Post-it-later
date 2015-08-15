from django.contrib.auth.models import User
from django.db import models

from queue.models import Bots

optional = {
    'blank': True,
    'null': True
}


class UserProfile(models.Model):

    user = models.ForeignKey(User, related_name='profile')
    coins = models.IntegerField(default=0)
    bots = models.ManyToManyField(Bots)

    def __unicode__(self):
        return "{}".format(self.user.get_full_name())

    @property
    def available_choices(self):
        choices = list(Bots.social_media_choices)
        unlocked_bots = [bot.social_media for bot in self.bots.all()]

        for choice in list(Bots.social_media_choices):
            if choice[0] not in unlocked_bots:
                choices.remove(choice)
        return tuple(choices)


class Achievement(models.Model):

    name = models.CharField(max_length=255)
    minimum_posts = models.IntegerField()
    reward = models.IntegerField()

    def __unicode__(self):
        return self.name


class Redeem(models.Model):

    achievement = models.ForeignKey(Achievement)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return "{}".format(self.user.get_full_name())