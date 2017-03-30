from NeuroPy import NeuroPy
from time import *

mindWave = NeuroPy("/dev/tty.MindWaveMobile-DevA", 57600)
mindWave.start()


def func(val):
    if val % 2 == 0:
        print "much success"
    else:
        print "wow"

mindWave.setCallBack("rawValue", func)

sleep(10)
