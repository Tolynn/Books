from django.shortcuts import render_to_response
from django.template.context_processors import csrf

def my_view(request):
    csrf = unicode(csrf(request)['csrf_token'])


