################################################################################
# Example Ultrasonic sensor HC-SR04
#
# Created: 2016-03-20 20:46:00
# The value 1 means out of range
# Range is between 2cm and 400cm
# The distance is always an int value
################################################################################

from community.matrix866.hcsr04 import hcsr04

import streams
streams.serial()


try:
    sleep(5000)
    print("starting")
    #A = hcsr04.HCSR04(TRIGGERPORT,ECHOPORT.ICU)
    A = hcsr04.HCSR04(D0,D1.ICU)
    #With A.Distance() you get the distance value
    #But if you don't read the value with ReadDistance() before
    #you get: None
    print(A.Distance())
    #You can directly access the value with:
    print(A.distance)
    sleep(3000)
        

    #After the readDistance() the distance is calculated
    A.ReadDistance()
    print(A.Distance())
    
    sleep(3000)
    
    #You can do ReadDistance() + Distance() with GetDistance() in oneshot
    print(A.GetDistance())
    
except Exception as DistanceError:
    print(DistanceError)