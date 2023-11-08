import random
from time import sleep
from helpers import modes
from helpers import connectWIFI


m = []
m.extend(range(5))
print(m)
brt = 0.4
# mode = modes.Modes()
# Mode = random.choice(m)
# mode.modeSelect(Mode)

wifi = connectWIFI.ConnectWIFI()

wifi.disconnect()
sleep(5)

ip = wifi.connect()
connection = wifi.open_socket(ip)
print(connection)


try:
    while True:
        sleep(.25)
        wifi.serve(connection)

except KeyboardInterrupt:
        print("Interupted")
        wifi.disconnect()
        sleep(5)
        print("Exiting....")
        
        
