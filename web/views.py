from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect


def home(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('export'))
    return render_to_response('index.html', {}, RequestContext(request))


@login_required
def export(request):
    #TODO
    return render_to_response('done.html', {'user': request.user}, RequestContext(request))