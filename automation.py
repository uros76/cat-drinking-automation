import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)         #Read output from PIR motion sensor
GPIO.setup(12, GPIO.IN)         #Read HIGH from stop switch
GPIO.setup(3, GPIO.OUT)         #Relay output pin
x=1                             #State variable

while True:
    i=GPIO.input(11)            #motion sensor
    s=GPIO.input(12)            #switch

    if s==0: #Switch OFF
        GPIO.output(3, GPIO.HIGH) #Turn OFF Relay
        x=1
        time.sleep(1)

    elif s==1 and x==1: #Switch ON first time
        x=0
        GPIO.output(3, GPIO.HIGH) #Turn OFF Relay
        time.sleep(30)            #wait delay before first sensing
        continue

    elif s==1:
        if i==0: #Switch ON movement OFF
            GPIO.output(3, GPIO.HIGH) #Turn OFF Relay
            time.sleep(1)

        elif i==1: #Switch ON movement ON
            GPIO.output(3, GPIO.LOW)  #Turn ON Relay
            time.sleep(70)            #Relay ON delay in seconds
            GPIO.output(3, GPIO.HIGH) #Turn OFF Relay to prevent repeat sense
            time.sleep(90)            #Sensing stopped in seconds

    time.sleep(0.1)
