try:
    import RPi.GPIO as GPIO
    import time
except RuntimeError:
    print('import fail')
    
led_pin = 12

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(led_pin, GPIO.OUT)
    GPIO.output(led_pin, 0)
    
def blinking():
    GPIO.output(led_pin, GPIO.HIGH)
    time.sleep(1.0)
    GPIO.output(led_pin, 0)
    time.sleep(1.0)
    
if __name__== '__main__':
    try:
        setup()
        while True:
            blinking()
    except KeyboardInterrupt:
        print('STOP!')
    finally:
        print('clean up')
        GPIO.cleanup()