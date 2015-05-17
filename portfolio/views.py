import json
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, RequestContext
from django.http import HttpResponse, HttpResponseRedirect

from django.utils.translation import (
	LANGUAGE_SESSION_KEY, check_for_language, get_language, to_locale,
)

from portfolio.models import Work, Tech, Article, Tag
from portfolio.forms import ContactForm


def wechat(request):
	return render(request, 'portfolio/view_wechat.html')

def view_index(request):
	
	try:
		aboutme = Article.objects.get(pk=1)
	except:
		aboutme = None
	
	tags = Tag.objects.all();
	
	#Contact form
	if request.method == 'GET':
		form = ContactForm()
	else:
		form = ContactForm(request.POST)
		if form.is_valid():
			from_email = form.cleaned_data['email']
			name = form.cleaned_data['name']
			subject = form.cleaned_data['subject']
			message = form.cleaned_data['message']
			
			try:
				send_mail(subject, message+" from "+name, from_email, ['potc.zone@gmail.com'])
			except BadHeaderError:
				pass
			#	return HttpResponse('Invalid header found.')
			#return redirect('thanks')
	
	context = {
		'aboutme' : aboutme,
		'tags' : tags,
		'form' : form,
	}
	
	return render(request, 'portfolio/view_index.html', context)

def view_work(request, tag_id=0):
	
	#works = Work.objects.all()
	techs = Tech.objects.all()
	tags = Tag.objects.all()
	
	if(tag_id):
		#works = works.filter(tags=tag_id);
		for t in tags:
			if t.id == int(tag_id):
				t.active = True
				
	
	context = {
		#'works' : works,
		'work_filters' : techs,
		'tags' : tags,
		'tags_selected' : tag_id,
	}
	
	return render(request, 'portfolio/view_work.html', context)

def worklist(request):
	results = {'success':False}
	if request.method == 'GET':
		GET = request.GET
        if GET.has_key(u'tags'):
			tagsRaw = GET[u'tags']
			
			# Query Works object
			works = Work.objects.all()
			
			if(len(tagsRaw)):
				tags = tagsRaw.split('_')
				results = {'success':True, 'data':tags}
			
			
			
			
				#create Q Object
				from django.db.models import Q
				tags_filter = Q()
				
				
				
				for tag in tags:
					q = Q(tags = tag)
					tags_filter = tags_filter | q
					
				works = works.filter( tags_filter ).distinct()
			
			context = RequestContext(request,{
				'works' : works,
			});
			
			from django.template.loader import render_to_string
			
			results['html'] = render_to_string('portfolio/worklist.html', context)
			
	return HttpResponse(json.dumps(results), content_type = "application/json")
	

def index(request):
	return view_index(request)
	
	works = Work.objects.all()
	
	"""
	w = works[0]
	title = w.title"""
	
	techs = Tech.objects.all()
	
	#aboutme = Article.objects.get(title="About me") #might be a pb with translation here
	#if not aboutme:
	#Make sure there is pk = 1 article otherwise crash... TODO
	aboutme = Article.objects.get(pk=1)
	
	
	
	context = RequestContext(request,{
		'works' : works,
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
