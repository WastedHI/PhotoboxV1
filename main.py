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
modesw = buttons.Pbswitch(PBSW1_PIN)
brtsw = buttons.Pbswitch(PBSW2_PIN)

def main():
    global BRIGHTNESS
    oldBRT = 0.0
    try:
        cmode = 0
        eff.modeSelect(cmode)
        while True:
            # Check if button was pressed and released, 
            # then do something based on length of button press.
            # If btn press was less then 1000ms then change mode. 
            # If more then 1000ms then set mode to 0 or off state

            modep,modesp,modelp = modesw.status()
            brtp,brtsp,brtlp = brtsw.status()

            if modep == True:
                if modelp == True:
                    modesw.reset()
                    cmode = 0
                    eff.modeSelect(cmode)
                elif modesp == True:
                    modesw.reset()
                    cmode += 1
                    if cmode >= 5:
                        cmode = 0
                    eff.modeSelect(cmode)
            if brtp == True:
                brtsw.reset()
                oldBRT = BRIGHTNESS
                BRIGHTNESS += .05
                if BRIGHTNESS >= 1.02:
                    BRIGHTNESS = 0.4
                print("Orig Brt = ", oldBRT, "New Brt = ", BRIGHTNESS)
                eff.updateBrt(BRIGHTNESS)
            time.sleep(.2)

    except KeyboardInterrupt:
        eff.clear()
        eff.clearDisp()

if __name__ == '__main__':
    main()