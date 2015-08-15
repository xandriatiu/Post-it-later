from __future__ import (
    absolute_import,
)

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from django.views.generic import TemplateView

from users import urls as users_urls

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(users_urls, namespace='users')),
	url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^login/', TemplateView.as_view(template_name='user/index.html')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
