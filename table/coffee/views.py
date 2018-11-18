# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, redirect, render
from django.core.urlresolvers import reverse
import json

from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime

from coffee.models import *
from coffee.forms import *

# Create your views here.
def IndexView(request):
    template_name = 'coffee/index.html'

    patternaddform = PatternAddForm(prefix='patternadd')

    context = {'patternaddform':patternaddform, }
    return render(request,'coffee/index.html', context)

def AddPatternView(request):
    f = PatternAddForm(request.POST,prefix='patternadd')

    if f.is_valid():

        new_pattern = f.save()
        return HttpResponse(json.dumps({"message": "Pattern Added"}), content_type="application/json", status=200)

    else:
        print 'invalid'
        print f.errors
        return HttpResponse(json.dumps({"message": "Pattern Error"}), content_type="application/json", status=400)

def LoadPatternView(request):
    id = request.GET.get('id',None)

    try:
        pattern = Pattern.objects.get(pk=id)
    except ObjectDoesNotExist:
        return HttpResponse(json.dumps({"message": "No such pattern"}), content_type="application/json", status=200)
  
    response = {'Name':pattern.Name,
                'Gcode':pattern.Gcode.url,
                'Blueprint':pattern.Blueprint.url,
                'Photo':pattern.Photo.url,
                'Duration':pattern.Duration.strftime("%H:%M:%S"),
                'Description':pattern.Description,
                'Type':pattern.Type
                }
    print response
    
    return HttpResponse(json.dumps(response), content_type="application/json", status=200)

def CountPatternsView(request):

    n = Pattern.objects.all().count()
    pks = [x.pk for x in Pattern.objects.all()]
    print n, pks
    
    response = {'Count':n,
                'pks':pks
                }
    print response
    
    return HttpResponse(json.dumps(response), content_type="application/json", status=200)
