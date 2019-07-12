
names={'D1:0E:28:2D:71:AA':{'Name':"Puck1", 'DM':3}, 'B2:2B:0A:54:1C:82':{'Name':"ITAG1",'DM':10}, 'F3:0D:B4:19:E1:9D':{'Name':"Tile", 'DM':10}}
#names={'D1:0E:28:2D:71:AA':{'Name':"Puck1", 'DM':3}}

from bluepy import btle
import struct

class MyDelegate(btle.DefaultDelegate):
    def __init__(self,params):
        btle.DefaultDelegate.__init__(self)

    def handleNotification(self,cHandle,data):
        print("handling notification...")
##        print(self)
##        print(cHandle)
        print(struct.unpack("b",data))

#p = btle.Peripheral('F3:0D:B4:19:E1:9D', "random")
p = btle.Peripheral('D1:0E:28:2D:71:AA', "random")
p.setDelegate(MyDelegate(0))

services=p.getServices()
characteristics=p.getCharacteristics()

for sv in services:

    uuid=sv.uuid
    print (uuid.getCommonName())

for ch in characteristics:

    if ch.supportsRead():

        print (ch.getHandle())
        print (ch.read())


#while True:
 #   if p.waitForNotifications(1.0):
  #      continue
   # print("waiting...")
