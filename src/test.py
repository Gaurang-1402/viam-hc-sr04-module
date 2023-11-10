import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
trig_pin = 23
echo_pin = 24
GPIO.setup(trig_pin, GPIO.OUT)
GPIO.setup(echo_pin, GPIO.IN)

try:
    while True:
        
        GPIO.output(trig_pin, 0)
        time.sleep(2E-6)
        GPIO.output(trig_pin, 1)
        time.sleep(10E-6)
        GPIO.output(trig_pin, 0)
        
        # hang the echo pin
        while GPIO.input(echo_pin) == 0:
            pass
        
        echo_start_time = time.time()
        while GPIO.input(echo_pin) == 1:
            pass
        
        echo_stop_time = time.time()
        
        ping_travel_time = echo_stop_time - echo_start_time
        
        distance = 767 * ping_travel_time * 5280 * 12 /3600
        distance = distance / 2
        print(round(distance, 1, "Inches"))
        time.sleep(.2)
        
except KeyboardInterrupt():
    GPIO.cleanup()
    print("GPIO Good to go")