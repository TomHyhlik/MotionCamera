from time import sleep
import RPi.GPIO as GPIO
import sys
import os

f = open("output.txt", 'w')
sys.stdout = f

GPIO.setmode(GPIO.BCM)     # set up BCM GPIO numbering

# Set up the PIR input pin
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Set up LED output
GPIO.setup(20, GPIO.OUT)

# Callback function to run when motion detected
def motionSensor(channel):
    global counter
    GPIO.output(20, GPIO.LOW)
    if GPIO.input(21):     # True = Rising
        counter += 1
        GPIO.output(20, GPIO.HIGH)
        print 'Motion number:', counter
        os.system ("./camPhoto.sh")

# add event listener on pin 21
GPIO.add_event_detect(21, GPIO.BOTH, callback=motionSensor, bouncetime=300) 
counter = 0


try:
    while True:
        sleep(1)         # wait 1 second

finally:                   # run on exit
    GPIO.cleanup()         # clean up
    print "All cleaned up."
    f.close()
