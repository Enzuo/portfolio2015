from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf import settings

urlpatterns = [
	# Examples:
	# url(r'^$', 'myportfolio.views.home', name='home'),
	# url(r'^blog/', include('blog.urls')),
	
	url(r'^admin/', include(admin.site.urls)),  
	url(r'^redactor/', include('redactor.urls')),
	#url(r'^$', include('portfolio.urls')),
	url(r'^', include('portfolio.urls')),

]

if settings.DEBUG:
	urlpatterns += patterns(
		'django.views.static',
		(r'media/(?P<path>.*)',
		'serve',
		{'document_root': settings.MEDIA_ROOT}), )
	"""
	#to test pages 404 and 500 when debugging
	urlpatterns += patterns('',
		(r'^404/',
			'django.views.generic.simple.' \
			'direct_to_template',
			{'template': '404.html'}),
		(r'^500/',
			'django.views.generic.simple.' \
			'direct_to_template',
			{'template': '500.html'}))"""
