from machine import Pin
import time

#Pb_Switch = Pin(15,Pin.IN,Pin.PULL_DOWN)

class Pbswitch:
    def __init__(self, swPinNum):
        self.swPinNum = swPinNum
        self.pbState = 0
        self.mode = 0
        self.btnPressed = False
        self.longPress = False
        self.shortPress = False
        self.t1 = 0
        self.t2 = 0

        self.swName = Pin(self.swPinNum, Pin.IN,Pin.PULL_DOWN)
        self.pbState = self.swName.value() #Preset the STATE variable for the Pb_Switch
        self.startHandler()

    def Pb_Switch_INT(self,pin): # PB_Switch Interrupt handler
        
        self.swName.irq(handler=None) # Turn off the handler while it is executing

        if (self.swName.value() == 1) and (self.pbState == 0):  
            self.pbState = 1     # Update current state of switch
            self.btnPressed = True # Do required action here
            self.t1 = time.ticks_ms()

        elif (self.swName.value() == 0) and (self.pbState == 1): 
            self.pbState = 0     # Update current state of switch / Do required action here
            self.t2 = time.ticks_ms()
            dt = self.t2 - self.t1
            if dt >= 1000:
                self.longPress = True
                self.shortPress = False
            else:
                self.longPress = False
                self.shortPress = True

        self.swName.irq(handler=self.Pb_Switch_INT)
        
    def startHandler(self):

        #Setup the Interrupt Request Handling for Pb_Switch change of state
        self.swName.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING, handler=self.Pb_Switch_INT)

    def status(self):
        pressed = self.btnPressed
        shortPress = self.shortPress
        longPress = self.longPress
        return pressed, shortPress, longPress

    def reset(self):
        self.btnPressed = False
        self.shortPress = False
        self.longPress = False

    # def longPressed(self):
    #     lpress = self.longPress
    #     return lpress

    # def resetLP(self):
    #     self.longPress = False

