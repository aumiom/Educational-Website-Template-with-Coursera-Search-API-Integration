from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.template import Context, loader



def index(request):
   omi = "omprakash"
   import urllib
   import json
   resp = urllib.urlopen('https://api.coursera.org/api/courses.v1?q=search&query=malware+underground').read()
   content = json.loads(resp)
   template = loader.get_template("myapp/index.html")
   context = {
      'omi': omi,
      'content' : content,  
    }
   return HttpResponse(template.render(context, request))

def search(request):
   form = data = request.GET.get('squery')
   url = "https://api.coursera.org/api/courses.v1?q=search&query=" + form
   omi = "omprakash"
   import urllib
   import json
   vari = form
   resp = urllib.urlopen('https://api.coursera.org/api/courses.v1?start=1&limit=3&q=search&query='+ vari).read()
   content = json.loads(resp)
   template = loader.get_template("myapp/search.html")
   context = {
      'omi': omi,
      'content' : content,
      'form' : form,
    }
   return HttpResponse(template.render(context, request))