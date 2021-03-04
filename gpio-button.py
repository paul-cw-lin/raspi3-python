import RPi.GPIO as GPIO
import time

button = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

for i in range(5):
    btn = GPIO.input(button)
    print ('GPIO%d = %d' % (button, btn))
    time.sleep(2.0)
    
GPIO.cleanup()