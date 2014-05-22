from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from person import views

urlpatterns = patterns('',
	url(r'^person/$', views.PersonList.as_view()).
	url(r'^person/(?))
	url(r'^person/(?P<pk>[0-9]+)/$', views.PersonDestroy.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)