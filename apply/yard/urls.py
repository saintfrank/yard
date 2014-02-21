from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required

from yard import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ciao.views.home', name='home'),
	url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
	url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': 'yard/'}),
	
	url(r'^$',  views.my_view , name ='index' ),
	url(r'applications/new$',  views.application_new , name ='application_new' ),
	url(r'applications/$',  login_required ( views.applications_list ) , name ='applications_list' ),
	url(r'applications/(?P<id>[-\w\d]+)/$',  views.applications_detail , name ='applications_detail' ),
	url(r'skills/new$',  views.skill_new , name ='skills_new' ),
	url(r'skills/$',  views.skills_list , name ='skills_list' ),
	url(r'skills/(?P<id>[-\w\d]+)/$',  views.skills_detail , name ='skills_detail' ),
	#url(r'api/companies/$',  views.api_companies_list , name ='api_companies_list' ),
	#url(r'api/companies/(?P<id>[-\w\d]+)/$',  views.api_companies_detail , name ='api_companies_detail' ),
	url(r'companies/new$',  views.company_new , name ='company_new' ),
	url(r'companies/$',  views.companies_list , name ='companies_list' ),
	url(r'companies/(?P<id>[-\w\d]+)/$',  views.companies_detail , name ='companies_detail' ),
	url(r'portals/new$',  views.portal_new , name ='portal_new' ),
	url(r'portals/$',  views.portals_list , name ='portals_list' ),
	url(r'portals/(?P<id>[-\w\d]+)/$',  views.portals_detail , name ='portals_detail' ),
	url(r'angu/$$',  views.angu , name ='angu' ),

)
