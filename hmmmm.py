import time
import random
import pyautogui as pag


i = 0
pag.FAILSAFE = False
size = pyautogui.size()

pag.hotkey('alt', 'shiftleft', 'printscreen')
time.sleep(0.125)
pag.press('enter')

while i > -1:
##    try:
    rx = random.randint(-25, 25)
    ry = random.randint(-25, 25)

    ri = random.randint(-1,2)
    
    i += 1

    ## this moves the mouse
    if i % 10 == 0:
        pag.moveRel(rx, ry)
    else:
        pass


    ## this presses arrow keys
    if 29 % random.randint(1, 1001) == 0:
        if ri == -1:
            pag.press('left')
            print('l')
        elif ri == 0:
            pag.press('right')
            print('r')
        elif ri == 1:
            pag.press('up')
            print('u')
        elif ri == 2:
            pag.press('down')
            print('d')
    else:
        pass

    ## this presses alt-f4

    if 29 % random.randint(1, 100000001) == 0:
        pag.hotkey('alt', 'f4')
        print('alt f4 time bois')

    ## this presses alt-tab

    if 29 % random.randint(1, 1000001) == 0:
        pag.hotkey('alt', 'tab')
        print('alt tab time bois')

    ## this presses Win.

    if 29 % random.randint(1, 10001) == 0:
        for i in range(10):
            pag.hotkey('Win')
            print('Win time bois')

    ## this presses Win+E

    if 29 % random.randint(1, 10001) == 0:
        for i in range(10):
            pag.hotkey('win', 'e')
            print('Win time bois')

    ## this presses the volume key

    if 29 % random.randint(1, 1001) == 0:
        for i in range(100):
            pag.press('volumeup')
            print('Up time bois')

    ## this clicks on things.
    if 29 % random.randint(1, 10001) == 0:
        pag.click(x=random.randint(0, size[0]), y=random.randint(0, size[1]))
        print('click clack')

    if 29 % random.randint(1, 100001) == 0:
        pag.drag(x=random.randint(0, size[0]), y=random.randint(0, size[1]))
        print('get drugged')

    
##    except KeyboardInterrupt:
##        print('can\'t stop this')
##        pass
