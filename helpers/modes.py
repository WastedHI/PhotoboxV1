from helpers import effect


class Modes:
    def __init__(self):
        print("Modes __init__")

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
        modeSetting = Mode0
        return modeSetting
    def Mode1(self):
        modeSetting = Mode1
        return modeSetting
    def Mode2(self):
        modeSetting = Mode2
        return modeSetting
    def Mode3(self):
        modeSetting = Mode3
        return modeSetting
    def Mode4(self):
        modeSetting = Mode4
        return modeSetting

