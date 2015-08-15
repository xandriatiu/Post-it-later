from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponseRedirect
from django.core import urlresolvers
from django.contrib import messages

from users.models import Achievement, Redeem, UserProfile
from queue.models import Bots
from unlockpaidfeatures.forms import BotsForms

class SettingsView(View):

    def get(self, request, *args, **kwargs):
        context = {}
        context['bots'] = UserProfile.object.get('bots')
        coins = UserProfile.object.get('coins')
        price = Bots.object.get('price')
        image = Bots.object.get('image')
        for bot in bots
            if coins >= price
                image = 
            return render(request, 'user/test.html', context)
