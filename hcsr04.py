################################################################################
# Ultrasonic Sensor HC-SR04
#
# Created: 2016-03-11 00:22:22.157177
#
################################################################################

import icu


class HCSR04:

    def __init__(self,triggerPort,echoPort):
        self.distance = None
        self.triggerPort = triggerPort
        self.echoPort = echoPort
        pinMode(self.triggerPort,OUTPUT)
        pinMode(self.echoPort,INPUT)

    def ReadDistance(self): 
        """This method calculate the distance and save it as class attribute, does not return anything"""
        raw_distance = 0
        sleep(60)#SR04 datasheet advice 60ms between two measurements
        digitalWrite(self.triggerPort,LOW)
        sleep(2,MICROS)
        digitalWrite(self.triggerPort,HIGH)
        sleep(10,MICROS)

        digitalWrite(self.triggerPort,LOW)
        elapsed_time = icu.capture(self.echoPort,LOW_TO_HIGH,1,23200,MICROS)

        # Some detail from sr04 datasheet:    
        # 23200 and 116 equals to 400cm and 2cm the range of the sensor
        # 23200 = 58*400; 116 = 58*2 
        # when it goes out or range (2 to 400 centimeters) elapsed_time is empty
        if elapsed_time:
            raw_distance=elapsed_time[0]/58
        else:
            raw_distance = 1

        self.distance = int(raw_distance)

    def Distance(self):
        """Returns the distance previously calculated with readDistance() method or with getDistance() method."""
        return self.distance

    def GetDistance(self):
        """Calculate the distance with readDistance() then return it"""
        self.ReadDistance()
        return self.distance