from django.shortcuts import render, RequestContext
from django.http import HttpResponse, HttpResponseRedirect

from django.utils.translation import (
	LANGUAGE_SESSION_KEY, check_for_language, get_language, to_locale,
)

from portfolio.models import Work, Tech, Article, Tag



def view_index(request):
	
	aboutme = Article.objects.get(pk=1)
	tags = Tag.objects.all();
	
	context = {
		'aboutme' : aboutme,
		'tags' : tags
	}
	
	return render(request, 'portfolio/view_index.html', context)

def view_work(request):
	
	works = Work.objects.all()
	techs = Tech.objects.all()
	
	context = {
		'works' : works,
		'work_filters' : techs,
	}
	
	return render(request, 'portfolio/view_work.html', context)

def index(request):
	
	works = Work.objects.all()
	
	w = works[0]
	title = w.title
	
	techs = Tech.objects.all()
	
	#aboutme = Article.objects.get(title="About me") #might be a pb with translation here
	#if not aboutme:
	#Make sure there is pk = 1 article otherwise crash... TODO
	aboutme = Article.objects.get(pk=1)
	
	
	
	context = RequestContext(request,{
		'works' : works,
		'wtitle' : title,
		'work_filters' : techs,
		'aboutme' : aboutme,
	})
	
	return render(request, 'portfolio/index.html', context)
	
	
def languageSelect(request, lang_code):
	#if language == 'en' or language == 'fr' or language == 'zh':
	#	request.session['django_language'] = language
		
	response = HttpResponseRedirect('/')
	
	if lang_code and check_for_language(lang_code):
		if hasattr(request, 'session'):
			request.session[LANGUAGE_SESSION_KEY] = lang_code
		else:
			response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang_code,
								max_age=settings.LANGUAGE_COOKIE_AGE,
								path=settings.LANGUAGE_COOKIE_PATH,
								domain=settings.LANGUAGE_COOKIE_DOMAIN)
		
	return response
	#return HttpResponse('coucou ' +lang_code+ ' '+request.session[LANGUAGE_SESSION_KEY])
