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
    
    sleep(3000)
    print("inizio")
    while True:
        a = HCSR04(D1,D2.ICU) # Create object
        a.distance            #Initialized with a None value
        
        a.readDistance()     #Value is now stored
        a.distance()         # Return the the value
        a.distance           # You can directly access teh value

        print( a.distance() )
        print( a.distance )
        
        
        print("Calculating distance again, wait...")
        
        #This equals to a.readDistance() + a.distance()
        #If you do this the old a object is overwritten with the new object a with a new distance value
        a.getDistance()      
        
        print( a.getDistance() )
        

        
except Exception as e1:
    print(e1)