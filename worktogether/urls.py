from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
admin.autodiscover()


urlpatterns = patterns('',
                       url(r'^sendgrid/',
                           include('sendgrid_events.urls')),
                       url(r'^admin/',
                           include(admin.site.urls)),
                       url(r'^',
                           include('teamwork.urls')), )

urlpatterns += patterns('',
                        (r'^static/(?P<path>.*)$',
                         'django.views.static.serve',
                         {'document_root': settings.STATIC_ROOT}), )
