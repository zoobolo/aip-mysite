from django.http import HttpResponse 
from django.template import loader
#from django.shortcuts import render
#from django.template import loader

def index(request):
#    return render(request, 'home.html')
#    return HttpResponse("Hello, world. You're at the grant index.")
    template = loader.get_template('base.html')
    return HttpResponse(template.render(request))