

class Palette:
    def __init__(self,rgbType):

        self.rgbType = rgbType.lower()
        
        self.MasterColor = {
        "powder blue" : "147, 181, 198,0",
        "tea green" : "221, 237, 170,0",
        "naples yellow" : "240, 207, 101,0",
        "burnt sienna" : "215, 129, 106,0",
        "fuchsia rose" : "189, 79, 108,0",

        #Plaltte2
        "oxford blue" : "16, 37, 66,0",
        "bittersweet" : "248, 112, 96,0",
        "platinum" : "205, 215, 214,0",
        "khaki" : "179, 130, 70,0", #179,163,148,0
        "white" : "255, 255, 255,0",
        #Palette3
        "federal blue" : "7, 0, 77,0",
        "steel blue" : "45, 130, 183,0",
        "aquamarine" : "66, 226, 184,0",
        "dutch white" : "243, 223, 191,0",
        "light coral" : "235, 138, 144,0",

        "black" : "0, 0, 0, 0",
        "red" : "255, 0, 0, 0",
        "yellow" : "255, 150, 0, 0",
        "green" : "0, 255, 0, 0",
        "cyan" : "0, 255, 255, 0",
        "blue" : "0, 0, 255, 0",
        "cream" : "255, 255, 214, 0",
        "purple" : "180, 0, 255, 0",
        "lavender" : "255, 153, 255, 0",

        "light blue" : "156, 255, 255, 0",
        "orange" : "255, 20, 0, 0"    
        }

        if self.rgbType == "sk6812":
            self.MasterColor["white"] = "0, 0, 0, 255"
       
    def parseColor(self,color):
        x = list(color.split(","))
        for i in range(len(x)):
            x[i] = int(x[i])
        color = tuple(x)
        return color

    def pickColor(self,color):
        color = color.lower()
        #self.palette = palette.lower()
        color = self.parseColor(self.MasterColor.get(color))
        return color

    def genColorList(self):
        self.lcolors = []

        for k,v in self.MasterColor.items():
            self.lcolors.append(k)
        print(self.lcolors)
        return self.lcolors

