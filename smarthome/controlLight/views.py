from django.shortcuts import render
from django.http import HttpResponse
#import RPi.GPIO as GPIO
import time

cocina=8
comedor=10
pasillo=12
sala=16
alcobapr=18
alcobamat=22
estudio=24
alcobava=26

"""GPIO.setmode(GPIO.BOARD)
GPIO.setup(comedor,GPIO.OUT)
GPIO.setup(pasillo,GPIO.OUT)
GPIO.setup(sala,GPIO.OUT)
GPIO.setup(alcobapr,GPIO.OUT)
GPIO.setup(alcobamat,GPIO.OUT)
GPIO.setup(estudio,GPIO.OUT)
GPIO.setup(alcobava,GPIO.OUT)

GPIO.output(sala,0)
GPIO.output(cocina,0)
GPIO.output(comedor,0)
GPIO.output(alcobapr,0)
GPIO.output(alcobamat,0)
GPIO.output(estudio,0)
GPIO.output(alcobava,0)
"""
def blinker(request):
    if 'sala' in request.POST:
        if request.POST.get('sala','')=='on':
            GPIO.output(sala,1)
        elif request.POST.get('sala','')=='off':
            GPIO.output(sala,0)
    elif 'cocina' in request.POST:
        if request.POST.get('cocina','')=='on':
            GPIO.output(cocina,1)
        elif request.POST.get('cocina','')=='off':
            GPIO.output(cocina,0)
    elif 'comedor' in request.POST:
        if request.POST.get('comedor','')=='on':
            GPIO.output(comedor,1)
        elif request.POST.get('comedor','')=='off':
            GPIO.output(comedor,0)
    elif 'pasillo' in request.POST:
        if request.POST.get('pasillo','')=='on':
            GPIO.output(pasillo,1)
        elif request.POST.get('pasillo','')=='off':
            GPIO.output(pasillo,0)
    elif 'alcobapr' in request.POST:
        if request.POST.get('alcobapr','')=='on':
            GPIO.output(alcobapr,1)
        elif request.POST.get('alcobapr','')=='off':
            GPIO.output(alcobapr,0)
    elif 'alcobamat' in request.POST:
        if request.POST.get('alcobamat','')=='on':
            GPIO.output(alcobamat,1)
        elif request.POST.get('alcobamat','')=='off':
            GPIO.output(alcobamat,0)
    elif 'estudio' in request.POST:
        if request.POST.get('estudio','')=='on':
            GPIO.output(estudio,1)
        elif request.POST.get('estudio','')=='off':
            GPIO.output(estudio,0)
    elif 'alcobava' in request.POST:
        if request.POST.get('alcobava','')=='on':
            GPIO.output(alcobava,1)
        elif request.POST.get('alcobava','')=='off':
            GPIO.output(alcobava,0)
    elif 'controltotal' in request.POST:
        if request.POST.get('controltotal','')=='on':
            GPIO.output(sala,1)
            GPIO.output(cocina,1)
            GPIO.output(comedor,1)
            GPIO.output(alcobapr,1)
            GPIO.output(alcobamat,1)
            GPIO.output(estudio,1)
            GPIO.output(alcobava,1)
        elif request.POST.get('controltotal','')=='off':
            GPIO.output(sala,0)
            GPIO.output(cocina,0)
            GPIO.output(comedor,0)
            GPIO.output(alcobapr,0)
            GPIO.output(alcobamat,0)
            GPIO.output(estudio,0)
            GPIO.output(alcobava,0)

    return render(request,'control_page.html')
