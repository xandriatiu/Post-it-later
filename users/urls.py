from django.conf.urls import url, include

from users.views import (
	DashboardView,
    LoginView,
    LogoutView,
)
from django.views.generic import TemplateView

from users import views


urlpatterns = [
    url(r'^dashboard/$',DashboardView.as_view(template_name='user/profile.html'), name="dashboard"),
    url(r'^logout$', LogoutView.as_view(), name="logout"),
    url(r'^payment-url/$', views.buy_my_item, name='pay'),
    url(r'^some/obscure/name/', include('paypal.standard.ipn.urls')),
    url(r'^$', LoginView.as_view(template_name='user/index.html'), name='login'),

]