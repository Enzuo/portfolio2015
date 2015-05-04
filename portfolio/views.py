from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	
	
	
	context = {
	}
	
	return render(request, 'portfolio/index.html', context)
	
	
def languageSelect(request, language):
	return HttpResponse('coucou ' +language)
