from django.conf.urls import url

from django.conf.urls import url, include

from users.views import (
    DashboardView,
    LoginView,
    LogoutView,
)
from users import views

urlpatterns = [
    url(r'^$', LoginView.as_view(), name="login"),
    url(r'^dashboard/$', DashboardView.as_view(), name="dashboard"),
    url(r'^logout/$', LogoutView.as_view(), name="logout"),
    url(r'^payment-url/$', views.buy_my_item),
    url(r'^some/obscure/name/', include('paypal.standard.ipn.urls')),
]