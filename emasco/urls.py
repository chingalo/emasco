from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    url(r'', include('home.urls')),
    url(r'', include('administration.urls')),
    #url(r'', include('services.urls')),
    url(r'', include('portfolio.urls')),
    url(r'', include('contacts.urls')),
    url(r'', include('emascouser.urls')),
    url(r'^admin/', include(admin.site.urls)),
    
    
    
)+ staticfiles_urlpatterns()


if settings.DEBUG:
    urlpatterns = patterns('',
		
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT,
        'show_indexes': True}),
        url(r'',
        include('django.contrib.staticfiles.urls')),
    ) + urlpatterns
