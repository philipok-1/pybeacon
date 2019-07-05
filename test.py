from sense_hat import SenseHat

import time
import random

sense = SenseHat()

red = (255, 0, 0)
blue = (0, 0, 255)


while True:

    rn=random.randint(0,8)
    print (rn)
    for i in range(0,rn):

        for j in range (7-i,8):
            cn=i+1
            sense.set_pixel(i,j, (50,150,30))

    time.sleep(.5)

    sense.clear()
