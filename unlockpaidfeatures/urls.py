from django.conf.urls import patterns, include, url

from unlockpaidfeatures.views import SettingsView

urlpatterns = patterns('',
    url(r'^settings/', SettingsView.as_view(), name='change'),
)