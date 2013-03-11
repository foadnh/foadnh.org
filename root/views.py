#from django.template import Context, loader
from django.template import RequestContext
from django.shortcuts import render_to_response
#from django.http import HttpResponse

def home(request):
#	t = loader.get_template('base.html')
#	c = Context(request)
#	return HttpResponse(t.render(c))
	return render_to_response('home.html', {'path': request.path},
								context_instance=RequestContext(request))

def about(request):
	#t = loader.get_template('base.html')
	#c = Context(request)
	#return HttpResponse(t.render(c))
	return render_to_response('about.html', {'path': request.path},
								context_instance=RequestContext(request))
