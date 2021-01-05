from pynput.mouse import Button, Controller
from time import sleep
mouse = Controller()

def Shoot(shootVar):
    if shootVar:
        print("Start Request - 01")
        sleep(1)
        x = 0
        while (x<100):
            x+=1
            print("pressed '" + str(x) + "' times")
            mouse.press(Button.left)
            #sleep(0.25)
            sleep(0.01)
            mouse.release(Button.left)
            
            
            #sleep(0.25)
    else:
        print("Stop Request - 02")