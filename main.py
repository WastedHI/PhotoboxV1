from helpers import effect
from helpers import buttons
import time
import random

## LED_TYPE = "WS2812B" or "SK6812"
LED_TYPE = "SK6812"
NUM_LEDS = 26
PIN_NUM = 28 # (GP)28 = Pin 34 on the PICO W
BRIGHTNESS = 0.4
INTERAL_LEDS = 16
EXTERNAL_LEDS = 10
PBSW1_PIN = 15
PBSW2_PIN = 13
PBSW1_NAME = "Mode"

eff = effect.Effects(LED_TYPE, NUM_LEDS, PIN_NUM, BRIGHTNESS, INTERAL_LEDS, EXTERNAL_LEDS)
eff.details()
pb1 = buttons.Pbswitch(PBSW1_PIN)
pb2 = buttons.Pbswitch(PBSW2_PIN)

def main():
    global BRIGHTNESS
    oldBRT = 0.0
    try:
        cmode = 0
        eff.modeSelect(cmode)
        while True:
            time.sleep(.1)
            if pb1.pressed() == True:
                pb1.reset()
                cmode += 1
                if cmode >= 5:
                    cmode = 0
                eff.modeSelect(cmode)
            if pb2.pressed() == True:
                pb2.reset()
                print("SW2 pressed")
                oldBRT = BRIGHTNESS
                BRIGHTNESS += .05
                if BRIGHTNESS >= 1.02:
                    BRIGHTNESS = 0.4
                print("Orig Brt = ", oldBRT, "New Brt = ", BRIGHTNESS)
                eff.updateBrt(BRIGHTNESS)

    except KeyboardInterrupt:
        print("Good Bye")
        eff.clear()
        eff.clearDisp()

if __name__ == '__main__':
    main()