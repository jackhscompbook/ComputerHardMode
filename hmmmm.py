

import random
import pyautogui as pag


i = 0
pag.FAILSAFE = False

while i > -1:
##    try:
    rx = random.randint(-35, 35)
    ry = random.randint(-35, 35)

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
##        pag.hotkey('alt', 'f4')
        print('alt f4 time bois')

    ## this presses alt-tab

    if 29 % random.randint(1, 1000001) == 0:
        pag.hotkey('alt', 'tab')
        print('alt tab time bois')
    
##    except KeyboardInterrupt:
##        print('can\'t stop this')
##        pass
