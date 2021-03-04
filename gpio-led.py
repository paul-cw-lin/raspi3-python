import RPi.GPIO as GPIO
import time

LED = 12

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED,GPIO.OUT,initial=GPIO.LOW)

for i in range(10):
    GPIO.output(LED, GPIO.HIGH)
    time.sleep(1.0)
    GPIO.output(LED, GPIO.LOW)
    time.sleep(1.0)
    
GPIO.cleanup()