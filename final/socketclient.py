import sensors
import socket
import time

HOST,PORT='192.168.223.169',8000

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))

moist,water,co=sensors.initialize()

t=time.time()
water_on_time=False
water_on=False
water_low=0
while True:
    
    last_water_on=water_on
    
    if water_on_time:
        if time.time()-water_on_time > 10:
            water_low=1
    
    mv,wv,cv,water_on=sensors.getvalues(moist,water,co,water_low)
    
    if last_water_on==False and water_on==True:
        water_on_time=time.time()
    if last_water_on==True and water_on==False:
        water_on_time=False
    print(water_low, water_on_time)
    if mv>0.3:
        water_low=0
    
    wv = -2.22*wv+2.22
    value=str(mv)+'/'+str(4*wv)+'/'+str(cv)+'/'+str(water_low)    
    response=value.encode('utf-8')
    if time.time()-t>5:
        s.send(response)
        print('message send')
        t=time.time()
        
        
print('finish')