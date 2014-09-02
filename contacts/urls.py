from django.conf.urls import patterns, url


from contacts import views

urlpatterns = patterns('',
    url(r'^send-message/$', views.contactMessage, name='contactMessage'),
    url(r'^all-messages/(?P<user_id>\d+)$', views.allMessages, name='allMessages'),
    url(r'^new-messages/(?P<user_id>\d+)$', views.newMessages, name='newMessages'),
    url(r'^message/(?P<message_id>\d+)/(?P<user_id>\d+)$', views.message, name='message'),
    
    )
