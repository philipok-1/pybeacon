from bluepy.btle import Scanner, DefaultDelegate

import time
import os

class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)


    def HandleDiscovery(self,dev,new_dev,new_dat):
        if new_dev:
            pass
        if new_dat:
            pass
        
scanner = Scanner().withDelegate(ScanDelegate())


#names={'D1:0E:28:2D:71:AA':{'Name':"Puck1", 'DM':3}, 'B2:2B:0A:54:1C:82':{'Name':"ITAG1",'DM':10}, 'F3:0D:B4:19:E1:9D':{'Name':"Tile", 'DM':10}}
names={'D1:0E:28:2D:71:AA':{'Name':"Puck1", 'DM':3}}


def get_distance(rssi):


    if rssi<=-70:

        output="Far"
    elif rssi<=-60:

        output="Getting closer"

    elif rssi<=-50:

        output="Close"

    elif rssi<=-30:

        output="Very close!"

    return output

while True:

    devices= scanner.scan(1.25)

    for dev in devices:
        print ("Device %s (%s), RSSI=%d dB" % (dev.addr, dev.addrType, dev.rssi))
        ID=dev.addr.upper()
    
        if ID in names:

            print (names[ID]['Name'])
            print (dev.rssi)

        else:  print ("not found")

    time.sleep(2)
    os.system('clear')
