from django.conf.urls import patterns, include, url

from django.contrib import admin
from web_app import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'CommunityCams.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^$', views.home, name='home'),
    url(r'^home/$', views.home, name='home'),
	url(r'^protectyourneighborhood/$', views.protect_your_neighborhood, name='protect_your_neighborhood'),
	url(r'^howitworks/$', views.how_it_works, name='how_it_works'),
	url(r'^projectfounders/$', views.project_founders, name='project_founders'),
	url(r'^ourvision/$', views.our_vision, name='our_vision'),
)
