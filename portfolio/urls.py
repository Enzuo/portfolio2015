from django.conf.urls import patterns, url

from portfolio import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
	#url(r'^(?P<pk>[0-9]+)/', views.DetailView.as_view(), name='detail')
	url(r'lang/(?P<language>\D+)/', views.languageSelect, name='language'),
	#url(r'lang/fr/', views.languageSelect, name='language'),
)
