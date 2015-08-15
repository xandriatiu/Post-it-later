from django import forms

from queue.models import Bots

my_choices = Bots.social_media_choices

class BotsForms(forms.Form):
	choice = forms.ChoiceField(choices=my_choices)