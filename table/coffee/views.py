# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, redirect, render
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie, csrf_protect

import json

from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime

from coffee.models import *
from coffee.forms import *

# Create your views here.
def IndexView(request):
    template_name = 'coffee/index.html'


    if request.method == 'GET':

        patternaddform = PatternAddForm(prefix='patternadd')

        context = {'patternaddform':patternaddform,}
        return render(request,'coffee/index.html', context)

    elif request.method == 'POST':

        if "AddPattern" in request.POST:
            f = PatternAddForm(request.POST,request.FILES,prefix='patternadd')
            if f.is_valid():
                new_pattern = f.save()
                try:
                    print new_pattern.Gcode.url
                    print new_pattern.Photo.url
                    print new_pattern.Blueprint.url
                except Exception as e:
                    print e

            else:
                print 'invalid'
                print f.errors

        return redirect(reverse('coffee:index'))




@csrf_exempt
def AddPatternView(request):
    f = PatternAddForm(request.POST,request.FILES,prefix='patternadd')
    print request.POST
    print request.FILES
    if f.is_valid():
        gcode = request.FILES['Gcode']
        new_pattern = f.save(commit=True)
        try:
            print new_pattern.Gcode.url
            print new_pattern.Photo.url
            print new_pattern.Blueprint.url
        except Exception as e:
            print e

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
    #print response

    return HttpResponse(json.dumps(response), content_type="application/json", status=200)

def CountPatternsView(request):

    n = Pattern.objects.all().count()
    pks = [x.pk for x in Pattern.objects.all()]
    #print n, pks

    response = {'Count':n,
                'pks':pks
                }
    #print response

    return HttpResponse(json.dumps(response), content_type="application/json", status=200)
