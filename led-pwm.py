import RPi.GPIO as GPIO
import time

LED = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED,GPIO.OUT,initial=GPIO.LOW)

p=GPIO.PWM(LED, 1000)
p.start(0)

for i in range(3):
    for rat in range(0,101,10):
        p.ChangeDutyCycle(rat);
        time.sleep(0.1)
    for rat in range(100,-1,-10):
        p.ChangeDutyCycle(rat);
        time.sleep(0.1)
        
p.stop()
GPIO.cleanup()