from django.shortcuts import render

# Create your views here.
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.conf import settings
from django.shortcuts import redirect
# from django.db.models import Entry

allOpAreas = {
	"Milwaukee",
	"Chicago",
	"Kenosha"
}


def Login(TemplateView):
	template = loader.get_template('login.html')
	return HttpResponse(template.render())

def HomeView(TemplateView):
	if not TemplateView.user.is_authenticated():
		return redirect('http://127.0.0.1:8000/admin/logout')
	else:
		template = loader.get_template('index.html')
		context = RequestContext(TemplateView, {'opAreas': allOpAreas} )
		return HttpResponse(template.render(context))
		return HttpResponse(template.render())

def OpAreaView(TemplateView):
	template = loader.get_template('opAreaIndex.html')
	context = RequestContext(TemplateView, {'pageTitle': 'OP AREA NAME', 'opAreas': allOpAreas} )
	return HttpResponse(template.render(context))
	