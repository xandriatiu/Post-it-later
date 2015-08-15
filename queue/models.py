from django.contrib.auth.models import User
from django.db import models

from adminsortable.models import Sortable
from djcelery.models import PeriodicTask

optional = {
    'blank': True,
    'null': True,
}


class Posts(models.Model):

    user = models.ForeignKey(User, related_name='posts')
    content = models.TextField()
    task = models.ForeignKey(PeriodicTask, **optional)
    bot = models.ForeignKey('Bots')
    status = models.BooleanField(default=False)

    def __unicode__(self):
        return "{}".format(self.user.get_full_name())

    class Meta:
        verbose_name_plural = 'Posts'


class Bots(Sortable):

    SMTP = 'smtp'
    FACEBOOK = 'facebook'
    TWITTER = 'twitter'
    PLURK = 'plurk'

    social_media_choices = (
        (SMTP, 'Email'),
        (FACEBOOK, 'Facebook'),
        (TWITTER, 'Twitter'),
        (PLURK, 'Plurk'),
    )

    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='bots')
    price = models.IntegerField()
    description = models.TextField()
    social_media = models.CharField(max_length=255, choices=social_media_choices)
    is_active = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name

    class Meta(Sortable.Meta):
        verbose_name_plural = "Bots"
