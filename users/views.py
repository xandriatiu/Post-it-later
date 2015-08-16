from django.contrib import auth
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core import urlresolvers
from django.views.generic import View

from braces.views import LoginRequiredMixin

	#paypal
from paypal.pro.views import PayPalPro

class DashboardView(LoginRequiredMixin, View):
				
	template_name = 'user/profile.html'

	def get(self, request, *args, **kwargs):
		context = {}
		if request.user.is_authenticated():
			return render(request, self.template_name, context)


class LoginView(View):

	template_name = 'user/index.html'

	def get(self, request, *args, **kwargs):
		context = {}
		if request.user.is_authenticated():
			return HttpResponseRedirect(urlresolvers.reverse('users:dashboard'))
		else: 
			return render(request, self.template_name, context)


class LogoutView(LoginRequiredMixin, View):

	template_name = 'user/index.html'
	context = {}

	def get(self, request, *args, **kwargs):
		auth.logout(request)
		return HttpResponseRedirect(urlresolvers.reverse('users:login'))



#paypal


def nvp_handler(nvp):
# This is passed a PayPalNVP object when payment succeeds.
# This should do something useful!
	pass

def buy_my_item(request):
    	item = {"paymentrequest_0_amt": "10.00",  # amount to charge for item
            "inv": "inventory",         # unique tracking variable paypal
            "custom": "tracking",       # custom tracking variable for you
            "cancelurl": "http://...",  # Express checkout cancel url
            "returnurl": "http://..."}  # Express checkout return url

	ppp = PayPalPro(
    	item=item,                            # what you're selling
    	payment_template="payment.html",      # template name for payment
    	confirm_template="confirmation.html", # template name for confirmation
    	success_url="/success/",              # redirect location after success
    	nvp_handler=nvp_handler,
    	)
	
	return ppp(request)
