# Create your views here.
# vim: ai ts=4 sts=4 et sw=4

from django.utils import simplejson
from django.http import HttpResponse
from django.shortcuts import render_to_response

def index(request):
    return render_to_response('snapchat/base.html')


def rpc(request):
    '''
    Delegates simple rpc requests.
    '''
    response_dict = {"text": "hello world!"}
    return HttpResponse(simplejson.dumps(response_dict), mimetype='application/javascript')
