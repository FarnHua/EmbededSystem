from bluepy.btle import Peripheral, UUID
from bluepy.btle import Scanner, DefaultDelegate

class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)
    def handleDiscovery(self, dev, isNewDev, isNewData):
        if isNewDev:
            print ("Discovered device", dev.addr)
        elif isNewData:
            print ("Received new data from", dev.addr)


class MyDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)
    def handleNotification(self, cHandle, data):
        print("Notification from Handle: 0x"+format(cHandle, '02X'))
        print(data)
        


scanner = Scanner().withDelegate(ScanDelegate())
devices = scanner.scan(10.0)
n=0
for dev in devices:
    print ("%d: Device %s (%s), RSSI=%d dB" % (n, dev.addr, dev.addrType, dev.rssi))
    n += 1
    for (adtype, desc, value) in dev.getScanData():
        print ("  %s = %s" % (desc, value))
number = input('Enter your device number: ')
print('Device', number)
print(devices[number].addr)

print ("Connecting...")
dev = Peripheral(devices[number].addr, 'random')
dev.setDelegate(MyDelegate())


print ("Services...")
for svc in dev.services:
    print (str(svc))

try:
    testService= dev.getServiceByUUID(UUID(0xfff0))
    #print("Handle    UUID                                  Properties")
    #print("----------------------------------------------------------")
    #for ch in testService.getCharacteristics():
     #   print (str(ch))
      #  if (ch.supportsRead()):
       #     print(str(ch.getHandle())    + '         ' +str(ch.uuid) + '    ' + ch.propertiesToString())
    cccd_handle = ''
    for descriptor in dev.getDescriptors():
        print(descriptor)
        if descriptor.uuid == 0x2902:
            print('Found')
            cccd_handle = descriptor.handle
            print(cccd_handle) #get fff4 cccd_handle not fff2
            
    dev.writeCharacteristic(cccd_handle, b"\x01\x00")
    while(1):
        if dev.waitForNotifications(1.0):
            print("Notification")
            continue
            
    print("Waiting")
        

finally:
    dev.disconnect()
