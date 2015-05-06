from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from django.utils.translation import (
	LANGUAGE_SESSION_KEY, check_for_language, get_language, to_locale,
)

from portfolio.models import Work





def index(request):
	
	works = Work.objects.all()
	
	w = works[0]
	title = w.title
	
	context = {
		'works' : works,
		'wtitle' : title,
	}
	
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
