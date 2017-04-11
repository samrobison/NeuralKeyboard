#test for keyboard output
from pymouse import PyMouse
from pykeyboard import PyKeyboard
from time import *

m = PyMouse()
k = PyKeyboard()

q = 0
while(q < 10):
    k.press_key('a')
    sleep(1)
    k.release_key('a')
    sleep(1)
    q += 1
