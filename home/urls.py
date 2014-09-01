from django.conf.urls import patterns, url

from home import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^login$', views.login, name='login'),
    url(r'^services$', views.services, name='services'),
    url(r'^portfolio$', views.portfolio, name='portfolio'),
    url(r'^mission-and-vision$', views.missionAndVision, name='missionAndVision'),
    url(r'^core-team$', views.coreTeam, name='coreTeam'),
    url(r'^contact-us$', views.contactUs, name='contactUs'),
   
    )
