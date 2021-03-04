import RPi.GPIO as GPIO
import time

button = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def button_pushed(channel):
    print('Pushed')
    
GPIO.add_event_detect(button, GPIO.BOTH, callback=button_pushed, bouncetime=500)

try:
    while True:
        print('Please push the button')
        time.sleep(2.0)
except KeyboardInterrupt: #when Ctrl+c
    print('STOP')
    
GPIO.remove_event_detect(button)
GPIO.cleanup()