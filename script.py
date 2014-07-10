import webiopi
 
GPIO = webiopi.GPIO
 
Rocket = 17 # GPIO pin using BCM numbering
 
 
# setup function is automatically called at WebIOPi startup
def setup():
    # set the GPIO used by the light to output
    GPIO.setFunction(Rocket, GPIO.OUT)
# loop function is repeatedly called by WebIOPi
def loop():
 
 
    # gives CPU some time before looping again
    webiopi.sleep(1)