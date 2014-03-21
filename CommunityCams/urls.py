from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'CommunityCams.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'', include('web_app.urls', namespace='web_app')),
    url(r'^admin/', include(admin.site.urls)),
)
