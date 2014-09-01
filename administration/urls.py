from django.conf.urls import patterns, url


from administration import views

urlpatterns = patterns('',
		url(r'^adminstrationMobo$', views.adminstrationMobo, name='adminstrationMobo'),
		url(r'^adminstration$', views.adminstration, name='adminstration'),
		url(r'^logout/(?P<user_id>\d+)$', views.logout, name='logout'),
		#url(r'^$', views.singlePortfolio, name='singlePortfolio'),
		)
