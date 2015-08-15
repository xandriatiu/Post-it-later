from django.contrib import auth
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import View

from braces.views import LoginRequiredMixin


class DashboardView(LoginRequiredMixin, View):
				
	template_name = 'user/login.html'

	def get(self, request, *args, **kwargs):
		context = {}
		if request.user.is_authenticated():
			return render(request, self.template_name, context)


class LoginView(View):

	template_name = 'user/index.html'

	def get(self, request, *args, **kwargs):
		context = {}
		if request.user.is_authenticated():
			return HttpResponseRedirect(reverse('users:dashboard'))
		else: 
			return render(request, self.template_name, context)


class LogoutView(LoginRequiredMixin, View):

	template_name = 'user/index.html'

	def get(self, request, *args, **kwargs):
		auth.logout(request)
		return HttpResponseRedirect(reverse('users:dashboard'))