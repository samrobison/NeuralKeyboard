#!/usr/bin/python

from NeuroPy import NeuroPy
from classifier import Classifier
from NK_Interface import NK_Interface
import Tkinter
#import gui class here
import time, sys


def main(argv):
    #start gui to train
    dir_list = [0,1,2,3,2,1,3,0,2,1,0,3,0,3,2,1,3,2,0,1]
    gui = NK_Interface(0,1,1, dir_list)
    gui.init_calib()
    data = gui.return_data()
    del gui
    #close gui after training data is added
    #train our classifier

    #c.train()
    # run function from driver that send key commands to the system





if __name__ == "__main__":
   main(sys.argv[1:])
