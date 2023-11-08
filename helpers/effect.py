from helpers import display
from helpers import rgbleds
from helpers import colors
import time
import random


class Effects:
    def __init__(self, LED_TYPE, NUM_LEDS, PIN_NUM, BRT, NUM_INT_LEDS, NUM_EXT_LEDS):
        self.ledType = LED_TYPE
        self.numLeds = NUM_LEDS
        self.pinNum = PIN_NUM
        self.brt = BRT
        self.oldBRT = 0.0
        self.intLeds = NUM_INT_LEDS
        self.extLeds = NUM_EXT_LEDS
        self.led = rgbleds.Led_init(LED_TYPE, NUM_LEDS, PIN_NUM)
        self.pal = colors.Palette(LED_TYPE)
        self.disp = display.Display()
        self.pastOledText = ''
        

        
        print("in effect.Effects __init__")

    def test1(self):
        print("in test1")

    def details(self):
        print("")
        print("======== Details ========")
        print("LED_TYPE = ", self.ledType)
        print("NUM_LEDS = ", self.numLeds)
        print("PIN_NUM = ", self.pinNum)
        print("BRT = ", self.brt)
        print("NUM_INT_LEDS = ", self.intLeds)
        print("NUM_EXT_LEDS = ", self.extLeds)
        print("=========================")
        print("")

    def clear(self):
        print("running clear...")
        self.led.pixels_fill(self.pal.pickColor("black"))
        self.led.pixels_show(self.brt)

    def clearDisp(self):
        self.disp.oledClear()

    def allFill(self, color):
        print("running allFill using ...")
        c = self.pal.pickColor(color)
        print(color,c)
        self.led.pixels_fill(self.pal.pickColor(color))
        self.led.pixels_show(self.brt)

    def discoLights(self,color,duration):
        print("running discoLights ...")
        self.clear()
        for i in range (0,duration):
            rled = random.randint(0, self.numLeds-1)

            self.led.pixels_set(rled, self.pal.pickColor(color))
            self.led.pixels_show(.9)
            self.led.pixels_set(rled, self.pal.pickColor("black"))
            time.sleep(.05)

    def intLights(self):
        int_index = []
        int_index.extend(range(self.intLeds))
        #print("internal led index's = ", int_index)
        return int_index

    def extLights(self):
        ext_index = []
        stop = self.intLeds + self.extLeds
        ext_index.extend(range(self.intLeds, stop))
        #print("external led index's = ", ext_index)
        return ext_index

    # def fillIntLights(self, color):
    #     x = self.intLights()
    #     print(x,x[5],x[0])
    #     for i in range(len(x)): #range(len(self.intLights()))
    #         print(i)
    #         ledIndex = x[i]
    #         self.led.pixels_set(ledIndex, self.pal.pickColor(color))
    #     self.led.pixels_show(self.brt)

    def fillIntLights(self, color):
        for i in range(len(self.intLights())): #range(len(self.intLights()))
            ledIndex = self.intLights()[i]
            self.led.pixels_set(ledIndex, self.pal.pickColor(color))
        self.led.pixels_show(self.brt)
        return color

    def fillExtLights(self, color):
        for i in range(len(self.extLights())): #range(len(self.intLights()))
            ledIndex = self.extLights()[i]
            self.led.pixels_set(ledIndex, self.pal.pickColor(color))
        self.led.pixels_show(self.brt)
        return color

    def modeSelect(self,mode):

        if mode == 0:
            print("In Mode 0 \n")
            self.Mode0()
        elif mode == 1:
            print("In Mode 1 \n")
            self.Mode1()
        elif mode == 2:
            print("In Mode 2 \n")
            self.Mode2()
        elif mode == 3:
            print("In Mode 3 \n")
            self.Mode3()
        elif mode == 4:
            print("In Mode 4 \n")
            self.Mode4()
        else:
            print("Wrong Mode selected \n")
        return mode

    def Mode0(self):
        print("Put mode 0 stuff here.")
        color1 = self.fillIntLights("black")
        color2 = self.fillExtLights("black")
        text = 'IntColor ' + color1 + ';' + 'ExtColor ' + color2
        self.pastOledText = text
        self.disp.oledWrite(self.disp.genText(text))

    def Mode1(self):
        print("Put mode 1 stuff here.")
        color1 = self.fillIntLights("white")
        color2 = self.fillExtLights("black")
        text = 'IntColor ' + color1 + ';' + 'ExtColor ' + color2
        self.pastOledText = text
        self.disp.oledWrite(self.disp.genText(text))

    def Mode2(self):
        print("Put mode 2 stuff here.")
        color1 = self.fillIntLights("white")
        color2 = self.fillExtLights("white")
        text = 'IntColor ' + color1 + ';' + 'ExtColor ' + color2
        self.pastOledText = text
        self.disp.oledWrite(self.disp.genText(text))

    def Mode3(self):
        print("Put mode 3 stuff here.")
        color1 = self.fillIntLights("green")
        color2 = self.fillExtLights("white")
        text = 'IntColor ' + color1 + ';' + 'ExtColor ' + color2
        self.pastOledText = text
        self.disp.oledWrite(self.disp.genText(text))

    def Mode4(self):
        print("Put mode 4 stuff here.")
        color1 = self.fillIntLights("federal blue")
        color2 = self.fillExtLights("federal blue")
        text = 'IntColor ' + color1 + ';' + 'ExtColor ' + color2
        self.pastOledText = text
        self.disp.oledWrite(self.disp.genText(text))

    def updateBrt(self,newbrt):
        self.oldBRT = self.brt
        self.brt = newbrt
        print(self.oldBRT, self.brt)
        print(len(self.pastOledText))
        if len(self.pastOledText) == 0:
            text = 'Old Brt ' + str(self.oldBRT) + ';' + 'New Brt ' + str(self.brt)
            
        text = 'Old Brt ' + str(self.oldBRT) + ';' + 'New Brt ' + str(self.brt)
        text = self.pastOledText + ';' + text
        self.disp.oledWrite(self.disp.genText(text))
        self.led.pixels_show(self.brt)

