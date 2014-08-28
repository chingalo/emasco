from django.conf.urls import patterns, url


from portfolio import views

urlpatterns = patterns('',
		url(r'^portfolio/(?P<portfolio_id>\d+)$', views.singlePortfolio, name='singlePortfolio'),
		)
