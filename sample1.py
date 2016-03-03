#!/usr/bin/python

# This is a simplest example to control a relay on/off per second.

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# init list with pin numbers

pin = 21

GPIO.setup(pin, GPIO.OUT)
GPIO.output(pin, GPIO.HIGH)

#main loop

try:
  while True:
    GPIO.output(pin, GPIO.LOW)
    print "Relay LOW"
    time.sleep(1)
    GPIO.output(pin, GPIO.HIGH)
    print "Relay HIGH"
    time.sleep(1)

# End program cleanly with keyboard
except KeyboardInterrupt:
  print "Exit program"
  GPIO.cleanup()

