################################################################################
# Example Ultrasonic sensor HC-SR04
#
# Created: 2016-02-06 15:24:45.274632
# The value 0 means the object is too close (<2cm)
# The value 1 means the object is too far (>400cm)
#    
################################################################################

from community.matrix866.hcsr04 import hcsr04

import streams
streams.serial()


try:
    sleep(2000)
    while True:
#         D1 = trigger port
#         D2.ICU = echo port
            x = hcsr04.getDistance(D1,D2.ICU)

            print("Distance:",x)
            sleep(1000)
except Exception as e1:
    print(e1)