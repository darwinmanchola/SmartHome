import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

vale=26
pulsador=3

GPIO.setup(vale,GPIO.OUT)
GPIO.setup(pulsador,GPIO.IN)

print("Inicio del programa")
GPIO.output(vale,0)



try:
    while True:
        #GPIO.output(vale,GPIO.input(pulsador))
        
        if(GPIO.input(pulsador)==0):
            print("pulsado")
            time.sleep(0.5)
            if (GPIO.input(vale)==0):
                GPIO.output(vale,1)
            else:
                GPIO.output(vale,0)
except KeyboardInterrupt:
    print("fin del programa")
    
