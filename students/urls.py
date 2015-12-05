from students import views
from django.conf.urls import patterns, url, include


urlpatterns = patterns('',
	
	url(r'^$', views.list_view, name='list_view'),
	url(r'^(?P<pk>\d+)/$', views.detail, name='detail'),
	url(r'add/$', views.create, name='add'),
	url(r'edit/(?P<pk>\d+)/$', views.edit, name='edit'),
	url(r'remove/(?P<pk>\d+)/$', views.remove, name='remove'),
	# url(r'^results/a\=(?P<a>\W{0,30}\w{0,30})\&b\=(?P<b>\W{0,30}\w{0,30})\&c\=(?P<c>\W{0,30}\w{0,30})/$', views.quadratic_results, name='quadratic_results'),
)
