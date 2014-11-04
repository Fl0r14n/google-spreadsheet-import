from django.shortcuts import render, render_to_response
from django.template import RequestContext

# Create your views here.


def home(request):
    if request.user.is_authenticated():
        return
    return render_to_response('index.html', {}, RequestContext(request))