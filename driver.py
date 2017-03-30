#!/usr/bin/python

from NeuroPy import NeuroPy
from classifier import Classifier
from NK_Interface import NK_Interface
import Tkinter
#import gui class here
import time, sys


def main(argv):
    #start gui to train
    gui = NK_Interface(0,1,1)
    gui.init_calib()
    #close gui after training data is added
    #train our classifier

    #c.train()
    # run function from driver that send key commands to the system





if __name__ == "__main__":
   main(sys.argv[1:])
