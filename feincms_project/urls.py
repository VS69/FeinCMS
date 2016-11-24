# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin


admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('feincms.contrib.preview.urls')),
    url(r'', include('feincms.urls'))
]

urlpatterns += patterns('',
                        url(r'^media/(?P<path>.*)$',
                            'django.views.static.serve',
                            {'document_root': settings.MEDIA_ROOT})
                        )
