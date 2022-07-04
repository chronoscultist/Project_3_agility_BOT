from login_function import login
import pyautogui as py
import time

log = login()

time.sleep(1)
# if it detects the osrs login screen image, it will initiate the re-logging process
if py.locateOnScreen("login_screen.PNG", confidence=0.80):
    log.login_time()

def agi(i):
    while i != 8:
        print("test"+str(i))
        loc = py.locateCenterOnScreen("stage_"+str(i)+".PNG", confidence=0.85)

        if loc != None:
            loc = py.moveTo(loc)
            py.click(loc)
            time.sleep(4.5)
            i = i+1
        elif i !=0:
            py.moveTo(loc)
            print(loc)
            if loc == None:
                i = 0
                while i != 1:
                    if py.locateCenterOnScreen("fail_1.PNG", confidence=0.60) != None:
                        loc = py.locateCenterOnScreen("fai1_3.JPG", confidence=0.6)
                        loc = py.moveTo(loc)
                        py.click(loc)
                        i = i+1
                        # NOTE TO SELF, FIXA VAD SOM SKA G ÖRAS NÄR BOTTEN RAMLAR.

    agi(0)
agi(1)


# after logging in, it will set the correct camera settings, the compass is corrupted
# it will reinitiate



