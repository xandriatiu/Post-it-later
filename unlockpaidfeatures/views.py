from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponseRedirect
from django.core import urlresolvers
from django.contrib import messages

<<<<<<< HEAD
from users.models import Achievement, UserProfile
=======
from users.models import Achievement, Redeem, UserProfile
>>>>>>> feff904eaad24188a6f39bef6a41b0dfa75cc846
from queue.models import Bots
from unlockpaidfeatures.forms import BotsForms

class SettingsView(View):

    def get(self, request, *args, **kwargs):
<<<<<<< HEAD
        user = request.user
        profile = user.profile.first()
        bots = profile.bots.all()
        coins = profile.coins

        botsmeta = []

        for bot, imgpair in zip(bots, (
            ('/static/img/R10.png', '/static/img/R11.png'),
            ('/static/img/R20.png', '/static/img/R21.png'),
            ('/static/img/R30.png', '/static/img/R31.png'),
            ('/static/img/R40.png', '/static/img/R41.png'),
        )):
            openimg, lockimg = imgpair
            botsmeta.append({
                'image': openimg if coins >= bot.price else lockimg,
                'bot': bot,
            })
        
        return render(request, 'user/achievements.html', {
            'botsmeta': botsmeta,
        })
=======
        context = {}
        context['bots'] = UserProfile.object.get('bots')
        coins = UserProfile.object.get('coins')
        price = Bots.object.get('price')
        image = Bots.object.get('image')
        for bot in bots
            if coins >= price
                image = 
            return render(request, 'user/test.html', context)
>>>>>>> feff904eaad24188a6f39bef6a41b0dfa75cc846
