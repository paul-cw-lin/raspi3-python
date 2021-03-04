import RPi.GPIO as GPIO
import time

button = 21
TIMEOUT = 10000

GPIO.setmode(GPIO.BCM)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

channel = GPIO.wait_for_edge(button, GPIO.RISING, timeout=TIMEOUT)

if channel:
    print('Rushed!')
else:
    print('Timeout')
    
GPIO.cleanup()