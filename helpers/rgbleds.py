#!/usr/bin/env python
# coding: utf-8

import array, time
from machine import Pin,I2C
import rp2
import random

class Led_init:
    def __init__(self, rgbStyle, numLeds, pinNum):
        print(Led_init)
        self.style = rgbStyle
        self.numLeds = numLeds
        self.pinNum = pinNum
        if self.style == "SK6812":
            self.start_sk_sm()
        else:
            self.start_ws_sm()
            
        #self.start_sm()
        self.details()

    def details(self):
        print("A strip of %2d " % (self.numLeds) + self.style + "'s has been configured")
        
    def start_sk_sm(self):
        @rp2.asm_pio(sideset_init=rp2.PIO.OUT_LOW, out_shiftdir=rp2.PIO.SHIFT_LEFT, autopull=True, pull_thresh=32) #was 24
        def sk6812():
            T1 = 2
            T2 = 5
            T3 = 3
            wrap_target()
            label("bitloop")
            out(x, 1)               .side(0)    [T3 - 1]
            jmp(not_x, "do_zero")   .side(1)    [T1 - 1]
            jmp("bitloop")          .side(1)    [T2 - 1]
            label("do_zero")
            nop()                   .side(0)    [T2 - 1]
            wrap()

        # Create the StateMachine with the ws2812 program, outputting on pin
        self.sm = rp2.StateMachine(0, sk6812, freq=8_000_000, sideset_base=Pin(self.pinNum))

        # Start the StateMachine, it will wait for data on its FIFO.
        self.sm.active(1)

        # Display a pattern on the LEDs via an array of LED RGB values.
        self.ar = array.array("I", [0 for _ in range(self.numLeds)])

    def start_ws_sm(self):
        @rp2.asm_pio(sideset_init=rp2.PIO.OUT_LOW, out_shiftdir=rp2.PIO.SHIFT_LEFT, autopull=True, pull_thresh=24) #was 24
        def ws2812b():
            T1 = 2
            T2 = 5
            T3 = 3
            wrap_target()
            label("bitloop")
            out(x, 1)               .side(0)    [T3 - 1]
            jmp(not_x, "do_zero")   .side(1)    [T1 - 1]
            jmp("bitloop")          .side(1)    [T2 - 1]
            label("do_zero")
            nop()                   .side(0)    [T2 - 1]
            wrap()

        # Create the StateMachine with the ws2812 program, outputting on pin
        self.sm = rp2.StateMachine(0, ws2812b, freq=8_000_000, sideset_base=Pin(self.pinNum))

        # Start the StateMachine, it will wait for data on its FIFO.
        self.sm.active(1)

        # Display a pattern on the LEDs via an array of LED RGB values.
        self.ar = array.array("I", [0 for _ in range(self.numLeds)])
        


    def pixels_show(self, brightness):
        if self.style == "SK6812": 
            dimmer_ar = array.array("I", [0 for _ in range(self.numLeds)])
            for i,c in enumerate(self.ar):
                r = int(((c >> 16) & 0xFF) * brightness)
                g = int(((c >> 24) & 0xFF) * brightness)
                b = int(((c >> 8) & 0xFF) * brightness)
                w = int((c & 0xFF) * brightness)
                dimmer_ar[i] = (g<<24) + (r<<16) + (b<<8) + w
            self.sm.put(dimmer_ar, 0) #8 to 0
            time.sleep_ms(10)
        else:
            
            dimmer_ar = array.array("I", [0 for _ in range(self.numLeds)])
            for i,c in enumerate(self.ar):
                r = int(((c >> 8) & 0xFF) * brightness)
                g = int(((c >> 16) & 0xFF) * brightness)
                b = int((c & 0xFF) * brightness)
                dimmer_ar[i] = (g<<16) + (r<<8) + b
            self.sm.put(dimmer_ar, 8)
            time.sleep_ms(10)
                
    def pixels_set(self, i, color):
        if self.style == "SK6812":
            self.ar[i] = (color[1]<<24) + (color[0]<<16) + (color[2]<<8) + color[3]
        else:
            self.ar[i] = (color[1]<<16) + (color[0]<<8) + color[2]

    def pixels_fill(self, color):
        for i in range(len(self.ar)):
            self.pixels_set(i, color)
