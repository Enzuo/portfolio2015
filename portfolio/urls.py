from django.conf.urls import patterns, url

from portfolio import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='site'),
    url(r'^index$', views.view_index, name='index'),
    url(r'^work$', views.view_work, name='work'),
	#url(r'^(?P<pk>[0-9]+)/', views.DetailView.as_view(), name='detail')
	url(r'lang/(?P<lang_code>\D+)/', views.languageSelect, name='language'),
	#url(r'lang/fr/', views.languageSelect, name='language'),
)
