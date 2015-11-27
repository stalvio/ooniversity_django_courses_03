from courses import views
from django.conf.urls import patterns, url, include


urlpatterns = patterns('',
	url(r'^(?P<pk>\d+)/', views.detail, name='detail'),
	# url(r'^results/a\=(?P<a>\W{0,30}\w{0,30})\&b\=(?P<b>\W{0,30}\w{0,30})\&c\=(?P<c>\W{0,30}\w{0,30})/$', views.quadratic_results, name='quadratic_results'),
)
