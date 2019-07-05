from bluepy.btle import Scanner, DefaultDelegate

import time
import os
import random

from sense_hat import SenseHat

sense = SenseHat()

sense.clear()

class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)


    def HandleDiscovery(self,dev,new_dev,new_dat):
        if new_dev:
            pass
        if new_dat:
            pass
        
scanner = Scanner().withDelegate(ScanDelegate())

def convert_db_to_integer(rssi):

    strength=rssi
    output=100-abs(strength)
    output=int(output/7)

    if output>8:  output=8

    elif output<0:  output=0

    return output

#names={'D1:0E:28:2D:71:AA':{'Name':"Puck1", 'DM':3}, 'B2:2B:0A:54:1C:82':{'Name':"ITAG1",'DM':10}, 'F3:0D:B4:19:E1:9D':{'Name':"Tile", 'DM':10}}
names={'D1:0E:28:2D:71:AA':{'Name':"Puck1", 'DM':3}}


while True:

    devices= scanner.scan(2)

    for dev in devices:
#        print ("Device %s (%s), RSSI=%d dB" % (dev.addr, dev.addrType, dev.rssi))
        ID=dev.addr.upper()
    
        if ID in names:

            print (names[ID]['Name'])
            print (dev.rssi)
            rn=convert_db_to_integer(dev.rssi)

            print (rn)

            for i in range(0,rn):

                for j in range (7-i,8):

                    sense.set_pixel(i,j, (rn*25,150,30))

            for i in range (rn,8):

                for j in range (7-i,8):

                    sense.set_pixel(i,j,(0,0,0))



    time.sleep(.5)
    os.system('clear')
