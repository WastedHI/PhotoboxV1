'''
Dealing with shared data so that both cores do not try to access the same data at the same
time.  A device known as a semaphore is used.

This is started with the command:
Data_key = _thread.allocate_lock() which creates a "lock and key system"

Anywhere data needs to be protected while we read it or write to it, we lock it then
release it so another process can use it.

The protected data in this example is Shared_Var which is heavily processed in the thread.
We lock access to that data using Data_Key.acquire() which is like turning the key to
lock the data.  When we are done processing the data, we release control using
Data_Key.release().

To prevent the data from being processed while we access it in another location, we perform
the same steps of aquire and release.  In this example we do that when we try to read the
data. Here again, we don't want that threaded process changing data while we are reading
it.

When an aquire command is executed, if access cannot be gained, the process will be held
until the other process releases control.  

'''
import machine, _thread
from time import sleep

Shared_Var = 0           #This is a variable both cores will access
exitvar = 0
Data_Key = _thread.allocate_lock() # create a semaphore -- fancy for a locking mechanism

def core_1():             #This function will be run in the second core
    from time import sleep #need to have this within core_1
    global Shared_Var     #because it is started with the _thread.start command
    global exitvar
    Counter = 0
    while True:	                            #Endless loop while True:
        Counter += 1
        print(Counter)                        #increment a counter 
        sleep(.5)                           #take a break
        Data_Key.acquire()                  #lock the following data up to .release
        print("Data locked")
        Shared_Var = 0                      #reset Shared_Var to zero
        while Shared_Var < 500000:          #loop 500,000 times
            Shared_Var += 1                 #incrementing Shared_Var to 500,000
        Shared_Var = Shared_Var + Counter   #add in the level 1 loop counter
        Data_Key.release()                  #unlock the preceeding data
        print("Data UN-locked")

        if exitvar == 1:
            print("Exit thread...")
            _thread.exit()

        
        
        
#main code
_thread.start_new_thread(core_1,()) #Starts the thread running in core 1

f=0
while True:
    f = f + 1
    sleep(.125)
    print("Fetching data")
    Data_Key.acquire()
    print(Shared_Var, " got it!", f)
    Data_Key.release()
    if f >= 20:
        break
exitvar = 1
sleep(10)
print("ALL DONE!")
