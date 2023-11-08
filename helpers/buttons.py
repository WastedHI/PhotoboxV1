from machine import Pin

#Pb_Switch = Pin(15,Pin.IN,Pin.PULL_DOWN)

class Pbswitch:
    def __init__(self, swPinNum):
        self.swPinNum = swPinNum
        
        self.pbState = 0
        self.mode = 0
        self.btnPressed = False

        self.swName = Pin(self.swPinNum, Pin.IN,Pin.PULL_DOWN)

        self.pbState = self.swName.value() #Preset the STATE variable for the Pb_Switch
        print("Pb_Switch State=", self.pbState)
        self.startHandler()

    def Pb_Switch_INT(self,pin): # PB_Switch Interrupt handler
        
        self.swName.irq(handler=None) # Turn off the handler while it is executing

        if (self.swName.value() == 1) and (self.pbState == 0):  
            self.pbState = 1     # Update current state of switch
            self.btnPressed = True
            print("ON")             # Do required action here 
                
        elif (self.swName.value() == 0) and (self.pbState == 1): 
            self.pbState = 0     # Update current state of switch
            print("OFF")         # Do required action here

        self.swName.irq(handler=self.Pb_Switch_INT)
        
    def startHandler(self):

        #Setup the Interrupt Request Handling for Pb_Switch change of state
        self.swName.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING,
         handler=self.Pb_Switch_INT)

    def pressed(self):
        pressed = self.btnPressed
        return pressed

    def reset(self):
        self.btnPressed = False
