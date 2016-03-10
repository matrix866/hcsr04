################################################################################
# Ultrasonic Sensor HC-SR04
#
# Created: 2016-03-11 00:22:22.157177
#
################################################################################

import icu
global distance#the calculated distance

def getDistance(triggerPort,echoPort): #example: getDistance(D1,D2.ICU)
        sleep(60)#SR04 datasheet advice 60ms between two measurements
        pinMode(triggerPort, OUTPUT)
        pinMode(echoPort, INPUT )

        digitalWrite(triggerPort,LOW)
        sleep(2,MICROS)
        digitalWrite(triggerPort,HIGH)
        sleep(10,MICROS)

        digitalWrite(triggerPort,LOW)
        elapsed_time = icu.capture(echoPort,LOW_TO_HIGH,1,100,MILLIS)
# 23200 and 116 equals to 400cm and 2cm the range of the sensor
# 23200 = 58*400; 116 = 58*2 
# from sr04 datasheet
        if elapsed_time[0] > 23200 or elapsed_time[0]<116:
           if elapsed_time[0] < 116:# distance is less then 2cm
                distance = 0
           else:
                distance = 1# distance is more then 400cm
        else:# distance is between 2 and 400 cm
            distance=elapsed_time[0]/58
        return distance