from django.conf.urls import url

from users.views import (
    DashboardView,
    LoginView,
    LogoutView,
)

urlpatterns = [
    url(r'^$', LoginView.as_view(), name="login"),
    url(r'^dashboard/$', DashboardView.as_view(), name="dashboard"),
    url(r'^logout/$', LogoutView.as_view(), name="logout"),
]