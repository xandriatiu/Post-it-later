from django.conf.urls import patterns, include, url

from unlockpaidfeatures.views import SettingsView

urlpatterns = patterns('',
    url(r'^$', SettingsView.as_view(), name='change'),
)