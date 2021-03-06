# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Hompage
    url(r'^$',TemplateView.as_view(template_name='homepage.html'),name="home"),
    
    # Admin
    url(r'^admin/', include(admin.site.urls)),
    url(r'^frontendadmin/', include('frontendadmin.urls')),
    url(r'^markitup/', include('markitup.urls')),
    
    # Apps
    url(r'^users/', include("users.urls", namespace="users")),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^events/', include('events.urls')),
    #url(r'^news/', include('news.urls')),
    #url(r'^photos/', include('photos.urls')),
    url(r'^slide/', include('slider.urls')),
    
    # Custom Pages

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

