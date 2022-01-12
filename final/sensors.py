from gpiozero import MCP3008
import time
import RPi.GPIO as GPIO





def initialize():
    moist=MCP3008(0)
    water=MCP3008(1)
    co=MCP3008(2)
    
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(17,GPIO.OUT)
    GPIO.output(17,GPIO.HIGH)

    GPIO.setup(27,GPIO.OUT)
    GPIO.output(27,GPIO.HIGH)

    return moist,water,co

def getvalues(moist,water,co,water_low):
    
    mv=moist.value
    wv=water.value
    cv=co.value
    
    water_on=False
    print('moisture:',mv,', water level:',-2.22*wv+2.22,', co=',cv)
    if wv > 0.6:
        GPIO.output(27,GPIO.LOW)
        
    else:
        GPIO.output(27,GPIO.HIGH)
    
    if mv>0.3 or water_low==1:
        water_on=False
        GPIO.output(17,GPIO.LOW)
        
    else:
        water_on=True
        GPIO.output(17,GPIO.HIGH)
        
    return mv,wv,cv,water_on


'''
moist=MCP3008(0)
water=MCP3008(1)

GPIO.setmode(GPIO.BCM)

GPIO.setup(17,GPIO.OUT)
GPIO.output(17,GPIO.LOW)

GPIO.setup(27,GPIO.OUT)
GPIO.output(27,GPIO.LOW)

while(True):
    print('moisture:',moist.value,', water level:',water.value)
    if moist.value<0.7:
        GPIO.output(27,GPIO.HIGH)
        print('water')
    else:
        GPIO.output(27,GPIO.LOW)
    
    if moist.value<0.7:
        GPIO.output(17,GPIO.HIGH)
        print('moist')
    else:
        GPIO.output(17,GPIO.LOW)
        
    time.sleep(0.1)
    '''