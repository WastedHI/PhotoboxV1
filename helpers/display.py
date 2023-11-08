# imports
from machine import Pin,I2C
from ssd1306 import SSD1306_I2C


class Display:

    def __init__(self):
        i2c_dev = I2C(0,scl=Pin(1),sda=Pin(0),freq=400000)
        self.oled = SSD1306_I2C(128, 64, i2c_dev)
        self.details()

    def details(self):
        print("oled disply has been configured")


    def genText(self, text):
        t = []
        t = text.split(";")
        print(t)
        return t

    def oledWrite(self,text):
        offset = 0
        self.oled.fill(0)
        for i in range(len(text)):
            self.oled.text(text[i],0,offset)
            offset = offset + 9
        self.oled.show()

    def oledClear(self):
        self.oled.fill(0)
        self.oled.show()

