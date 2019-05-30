
import time
import random
import pyautogui as pag
from threading import Thread 
import easygui as eg


pag.FAILSAFE = False
size = pag.size()

if eg.ynbox('Are you ready to start?', 'Ready', \
            ('Yea, let\'s go', 'No thanks')) == False:
    print('ok then')
    time.sleep(1)
    exit()

def main():
    m = Thread(target=jitter)
    m.start()
    t = Thread(target=start)
    t.start()
    time.sleep
    levels()

def jitter():
    i = 0
    while True:
        rx = random.randint(-25, 25)
        ry = random.randint(-25, 25)
        if i % 10 == 0:
            pag.moveRel(ry, ry)
        else:
            pass
        ++i
        
def start():
    pag.hotkey('alt', 'shiftleft', 'printscreen')
    time.sleep(0.125)
    pag.press('enter')
    i = 2
    while i > -1:
        try:
            
            ri = random.randint(-1,2)
            
            i += 1


            ## this presses arrow keys
            if 29 % random.randint(1, 1000001) == 0:
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

            if 29 % random.randint(1, 10000001) == 0:
                pag.hotkey('alt', 'tab')
                print('alt tab time bois')

            ## this presses Win.

            if 29 % random.randint(1, 10000001) == 0:
                for i in range(10):
                    pag.hotkey('Win')
                    print('Win time bois')

            ## this presses Win+E

            if 29 % random.randint(1, 100000001) == 0:
                for i in range(10):
                    pag.hotkey('win', 'e')
                    print('Win time bois')

            ## this presses the volume key

            if 29 % random.randint(1, 100000001) == 0:
                print('Up time bois')
                for i in range(100):
                    pag.press('volumeup')

            ## this clicks on things.
            if 29 % random.randint(1, 10000001) == 0:
                pag.click(x=random.randint(0, size[0]), \
                          y=random.randint(0, size[1]))
                print('click clack')

            if 29 % random.randint(1, 10000001) == 0:
                pag.dragTo(x=random.randint(0, size[0]), \
                         y=random.randint(0, size[1]))
                print('get drugged')

        
        except KeyboardInterrupt:
            print('can\'t stop this')
            pass

def levels():
    while True:
        eg.msgbox(msg='To win level 1, click the ok button!', \
                  title='1', ok_button='OK')
        if eg.boolbox('To win level 2, click the button which says \
"kjbkbjgf".', '2', ['kjbkbjgf', 'kjdkbjgf']):
            print('gg')
            break
        else:
            print('how?')
            continue
    eg.msgbox(msg='now that you\'ve done the levels, \
you get free play mode!')

if __name__ == '__main__':
    main()
