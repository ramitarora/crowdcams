from django.conf.urls import patterns, include, url

from django.contrib import admin
from web_app import views

admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'CommunityCams.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       url(r'^$', views.home, name='home'),
                       url(r'list/$', views.list, name='listing'),
                       url(r'^protectyourneighborhood/$', views.protect_your_neighborhood,
                           name='protect_your_neighborhood'),
                       url(r'^protectyourneighborhood/newpost$', views.new_post, name='new_post'),
                       url(r'^howitworks/$', views.how_it_works, name='how_it_works'),
                       url(r'^projectfounders/$', views.project_founders, name='project_founders'),
                       url(r'^ourvision/$', views.our_vision, name='our_vision'),
                       url(r'^accounts/register/$', views.register, name='user_registration'),
                       url(r'^accounts/login/$', views.login, name='user_login')
)
