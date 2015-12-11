from students import views
from django.conf.urls import patterns, url, include


urlpatterns = patterns('',
	
	url(r'^$', views.StudentListView.as_view(), name='list_view'),
	url(r'^(?P<pk>\d+)/$', views.StudentDetailView.as_view(), name='detail'),
	url(r'^edit/(?P<pk>\d+)/$', views.StudentUpdateView.as_view(), name='edit'),
	url(r'add/$', views.StudentCreateView.as_view(), name='add'),
	
	url(r'remove/(?P<pk>\d+)/$', views.StudentDeleteView.as_view(), name='remove'),
	# url(r'^results/a\=(?P<a>\W{0,30}\w{0,30})\&b\=(?P<b>\W{0,30}\w{0,30})\&c\=(?P<c>\W{0,30}\w{0,30})/$', views.quadratic_results, name='quadratic_results'),
)
