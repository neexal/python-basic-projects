import pyautogui as pg
import time

def screenshot():
    name = int(round(time.time() * 1000))
    name = '{}.png'.format(name)

    for i in range(5,0,-1):
        print('Capturing screenshot in ' + str(i))
        time.sleep(1)

    print('Capturing now!!!')
    image = pg.screenshot(name)
    image.show()

screenshot()
