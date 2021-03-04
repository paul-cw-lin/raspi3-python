import RPi.GPIO as GPIO
import time

button = 21
led = 12

GPIO.setmode(GPIO.BCM)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(led, GPIO.OUT, initial=GPIO.LOW)

def button_led(channel):
    GPIO.output(led, GPIO.LOW)
    time.sleep(1.0)
    GPIO.output(led, GPIO.HIGH)
    time.sleep(1.0)
    
GPIO.add_event_detect(button, GPIO.BOTH, callback=button_led, bouncetime=500)

try:
    while True:
        print('Please push the Button')
        time.sleep(2.0)
except KeyboardInterrupt:
    print('STOP!!')
    
GPIO.remove_event_detect(button)
GPIO.cleanup()