# import the libraries
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
relay = 26                   
initial_counter = 0
# set the pin numbers to be used from Broadcom chip

pushpin1 = 4 # assign a variable name to pin 17

GPIO.setup(pushpin, GPIO.IN) # set GPIO pin 17 as Input
GPIO.setup(pushpin, GPIO.IN) # set GPIO pin 17 as Input

while True:
  if (GPIO.input(pushpin1)):
    initial_counter = initial_counter + 1
    time.sleep(0.001)
    GPIO.output(relay,GPIO.HIGH)
    print(initial_counter)
GPIO.output(relay,GPIO.LOW)
