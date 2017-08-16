from django.shortcuts import render ,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import loader
from .models import Device
import RPi.GPIO as GPIO

devices = Device.objects.all()
GPIO.setmode(GPIO.BOARD)
for device in devices:
        GPIO.setup(int(device.gpio),GPIO.OUT)
        GPIO.output(int(device.gpio),0)
        device.state=False
        device.save()
        

def Home(request):
	devices = Device.objects.all()
	template=loader.get_template("index.html")
	context={
		'devices':devices
	}

	return HttpResponse(template.render(context,request))

def ActionDevice(request):
	action= request.POST['action']
	device=get_object_or_404(Device, pk=request.POST['device'])
	if action=='ON':
		device.state=True
		device.save()
		
		GPIO.output(int(device.gpio),1)
		
	elif action=='OFF':
		device.state=False
		device.save()
		GPIO.output(int(device.gpio),0)
	devices = Device.objects.all()
	return HttpResponseRedirect('/')

def ControlTotal(request):
        action= request.POST['action']
	devices=Device.objects.all()
	if action=='ON':
                for device in devices:
                        device.state=True
                        device.save()
                        GPIO.output(int(device.gpio),1)
        elif action=='OFF':
                for device in devices:
                        device.state=False
                        device.save()
                        GPIO.output(int(device.gpio),0)
        return HttpResponseRedirect('/')
