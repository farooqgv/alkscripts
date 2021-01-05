import psutil
import keyboard  # using module keyboard
from pynput.keyboard import Key, Controller
kkeyboard = Controller()
from time import sleep
from moveMouse import Shoot

autorunEnabled = False
def checkIfProcessRunning(processName):
    '''
    Check if there is any running process that contains the given name processName.
    '''
    #Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

# Check if any chrome process was running or not.
if checkIfProcessRunning('VALORANT'):#Valorant is running
    print('RUNNING....')
    while True:  # making a loop
        try:  # used try so that if user pressed other than the given key error will not be shown
            
            if keyboard.is_pressed('=') and autorunEnabled is False:  # if key 'q' is pressed 
                
                autorunEnabled = True
                print('autorun => ON')
                
                
                kkeyboard.press('w')
                kkeyboard.press(Key.space)
                Shoot(autorunEnabled)
                
                
                #break  # finishing the loop
            elif (keyboard.is_pressed('=') and autorunEnabled is True):
                autorunEnabled = False
                print("autorun => OFF")
                #Shoot(autorunEnabled)
                

                
            
        except:
            break  # if user pressed a key other than the given key the loop will break

else:#Valorant is not running
    print('NOT running')