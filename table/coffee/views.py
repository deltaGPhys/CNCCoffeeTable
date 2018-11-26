# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseRedirect, HttpResponse, StreamingHttpResponse
from django.shortcuts import render_to_response, redirect, render
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie, csrf_protect
from django.http import JsonResponse
import json

from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime

from coffee.models import *
from coffee.forms import *

import serial
import time

# Create your views here.
def IndexView(request):
    template_name = 'coffee/index.html'


    if request.method == 'GET':

        patternaddform = PatternAddForm(prefix='patternadd')

        context = {'patternaddform':patternaddform,}
        return render(request,'coffee/index.html', context)

    elif request.method == 'POST':
        print "indexpost"
        if "AddPattern" in request.POST:
            f = PatternAddForm(request.POST,request.FILES,prefix='patternadd')
            if f.is_valid():
                new_pattern = f.save()

            else:
                print 'invalid'
                print f.errors
        #
        # elif "EditPattern" in request.POST:
        #     print request.POST
        #     f = PatternAddForm(request.POST,request.FILES,prefix='patternadd')
        #     if f.is_valid():
        #         new_pattern = f.save()
        #         try:
        #             print new_pattern.Gcode.url
        #             print new_pattern.Photo.url
        #             print new_pattern.Blueprint.url
        #         except Exception as e:
        #             print e
        #
        #     else:
        #         print 'invalid'
        #         print f.errors

        return redirect(reverse('coffee:index'))

@csrf_exempt
def SendWholeGcodeView(request):
    # which pattern are we working on?
    if request.method == 'GET':
        id = request.GET['id'];
    elif request.method == 'POST':
        id = request.POST.get('id')

    try:
        this_pattern = Pattern.objects.get(pk=id)
    except:
        return HttpResponse(json.dumps({"message": "Pattern Not Found"}), content_type="application/json", status=400)

    # Open g-code file
    Gcode = this_pattern.Gcode
    Gcode.open(mode='r')
    f = Gcode.readlines()

    try:
        s = serial.Serial('/dev/ttyUSB0',115200) # cu.wchusbserial1450 GRBL operates at 115200 baud. Leave that part alone.
        # Wake up grbl
        s.write(bytes("\r\n\r\n"))
        time.sleep(2)   # Wait for grbl to initialize
        s.flushInput()  # Flush startup text in serial input
    except Exception as e:
        print e
        return HttpResponse(json.dumps({"error": "Unable to Connect"}), content_type="application/json", status=400)

    for line in f:
        l = line.strip() # Strip all EOL characters for consistency
        print 'Sending: ' + l

    # Stream g-code to grbl
    for line in f:
        l = line.strip() # Strip all EOL characters for consistency
        print l
        print 'Sending: ' + l,
        s.write(bytes(l)+ bytes('\n')) # Send g-code block to grbl
        grbl_out = s.readline() # Wait for grbl response with carriage return
        print ': ' + grbl_out.strip()

    # Wait here until grbl is finished to close serial port and file.
    while 1<2:
        s.write("?")
        grbl_out = s.readline()

        if "Run" in grbl_out:
            time.sleep(1)
        elif "Idle" in grbl_out:
            break

    # Close file
    f.close()

    # Gcode = this_pattern.Gcode
    # Gcode.open(mode='r')
    # content = ''.join(Gcode.readlines())
    # try:
    #     s = serial.Serial('/dev/ttyUSB0',115200) # cu.wchusbserial1450 GRBL operates at 115200 baud. Leave that part alone.
    #     # Wake up grbl
    #     s.write(bytes("\r\n\r\n"))
    #     time.sleep(2)   # Wait for grbl to initialize
    #     s.flushInput()  # Flush startup text in serial input
    # except Exception as e:
    #     print e
    #     return HttpResponse(json.dumps({"error": "Unable to Connect"}), content_type="application/json", status=400)
    #
    #
    # for line in content:
    #     try:
    #         s.write(bytes(line)+bytes('\n'))
    #         #s.write(line + '\n') # Send g-code block to grbl
    #         grbl_out = s.readline() # Wait for grbl response with carriage return
    #         print line+': ' + grbl_out.strip()
    #     except Exception as e:
    #         print e
    #         return HttpResponse(json.dumps({"error": "Write Error"}), content_type="application/json", status=400)

    s.close()

    return HttpResponse(json.dumps({"message": "Pattern Complete"}), content_type="application/json", status=200)

@csrf_exempt
def OpenGcodeView(request):
    # which pattern are we working on?
    if request.method == 'GET':
        id = request.GET['id'];
    elif request.method == 'POST':
        id = request.POST.get('id')

    try:
        this_pattern = Pattern.objects.get(pk=id)
    except:
        return HttpResponse(json.dumps({"message": "Pattern Not Found"}), content_type="application/json", status=400)

    Gcode = this_pattern.Gcode
    Gcode.open(mode='r')
    content = ''.join(Gcode.readlines())
    print content

    print type(Gcode.read())
    response = {}
    response['Gcode'] = content
    response['Content-Type'] = 'text/plain; charset=utf8'
    response['message'] = "Gcode file opened"
    # return response

    return HttpResponse(json.dumps(response), content_type="application/json", status=200)

@csrf_exempt
def SendLineView(request):
    #return HttpResponse(json.dumps({"message": "sent"}), content_type="application/json", status=200)
    try:
        s = serial.Serial('/dev/ttyUSB0',115200) # cu.wchusbserial1450 GRBL operates at 115200 baud. Leave that part alone.
        # Wake up grbl
        s.write(bytes("\r\n\r\n"))
        time.sleep(2)   # Wait for grbl to initialize
        s.flushInput()  # Flush startup text in serial input
    except Exception as e:
        print e
        return HttpResponse(json.dumps({"error": "Unable to Connect"}), content_type="application/json", status=400)

    line = request.POST.get('line')
    #line = line.decode('utf8', 'replace').encode()
    line = bytes(line)


    try:
        s.write(line+bytes('\n'))
        #s.write(line + '\n') # Send g-code block to grbl
        grbl_out = s.readline() # Wait for grbl response with carriage return
        print line+': ' + grbl_out.strip()
    except Exception as e:
        print e
        return HttpResponse(json.dumps({"error": "Write Error"}), content_type="application/json", status=400)

    #s.close()

    return HttpResponse(json.dumps({"message": grbl_out.strip()}), content_type="application/json", status=200)


@csrf_exempt
def AddPatternView(request):
    f = PatternAddForm(request.POST,request.FILES,prefix='patternadd')

    if f.is_valid():
        new_pattern = f.save(commit=True)

        return HttpResponse(json.dumps({"message": "Pattern Added"}), content_type="application/json", status=200)

    else:
        print 'invalid'
        print f.errors
        return HttpResponse(json.dumps({"message": "Pattern Error"}), content_type="application/json", status=400)

@csrf_exempt
def EditPatternView(request):
    # which pattern are we working on?
    if request.method == 'GET':
        id = request.GET['id'];
    elif request.method == 'POST':
        id = request.POST.get('id')
    Gcode = None
    try:
        this_pattern = Pattern.objects.get(pk=id)
    except:
        return HttpResponse(json.dumps({"message": "Pattern Not Found"}), content_type="application/json", status=400)

    if request.method == 'GET':

        f = PatternAddForm(instance = this_pattern, prefix='patternadd')
        return JsonResponse({'form':f.as_p()})

    elif request.method == 'POST':
        print request.POST.keys()
        if 'Gcode' in request.POST.keys():
            Gcode = request.POST['Gcode']
        f = PatternAddForm(request.POST,request.FILES,instance = this_pattern,prefix='patternadd')
        if f.is_valid():
            f.save();
            if Gcode:
                this_pattern = Pattern.objects.get(pk=id)
                print this_pattern.Gcode
                this_pattern.Gcode = Gcode
                print Gcode
                this_pattern.save()
                print this_pattern.Gcode


        return HttpResponse(json.dumps({"message": "Pattern Edited"}), content_type="application/json", status=200)

    else:
        print 'invalid'
        print f.errors
        return HttpResponse(json.dumps({"message": "Pattern Edit Error"}), content_type="application/json", status=400)


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
