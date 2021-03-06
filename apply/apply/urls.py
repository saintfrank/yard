from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'apply.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

	url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
	url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),

	url(r'^', include('yard.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
