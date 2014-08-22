from django.conf.urls import patterns, url


from emascouser import views

urlpatterns = patterns('',
    url(r'^(?P<user_id>\d+)/singleMember$', views.singleMember, name='singleMember'),
    )
