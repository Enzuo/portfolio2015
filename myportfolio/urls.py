from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'myportfolio.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^admin/', include(admin.site.urls)), 
    url(r'^summernote/', include('django_summernote.urls')),   
    url(r'^$', include('portfolio.urls')),
    url(r'/*', include('portfolio.urls')),

]
