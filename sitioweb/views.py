from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
#probando nuevos cambios.
""""Hola """
def inicio(request):
	return render_to_response('inicio.html', context_instance=RequestContext(request))
