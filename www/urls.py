from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	# Examples:
	# url(r'^$', 'www.views.home', name='home'),
	# url(r'^www/', include('www.foo.urls')),
	url(r'^$', 'root.views.home'),
	url(r'^about/$', 'root.views.about'),

	# Admin documentation:
	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

	# Admin
	url(r'^admin/', include(admin.site.urls)),

	# Authentication pages that needed
	(r'^accounts/login/$', 'django.contrib.auth.views.login'),
	(r'^accounts/logout/$', 'django.contrib.auth.views.logout'),

	# Zinnia
	url(r'^blog/', include('zinnia.urls')),
	url(r'^comments/', include('django.contrib.comments.urls')),

	# SMS application
	url(r'^sms/$', 'sms.views.index'),
	url(r'^sms/(?P<contactURL>\w+)/$', 'sms.views.index'),
	url(r'^sms/(?P<contactURL>\w+)/(?P<smsStart>\d+)/(?P<step>\d+)/$'
											, 'sms.views.index'),
)
