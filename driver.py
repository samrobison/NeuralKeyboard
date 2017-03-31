#!/usr/bin/python

from NeuroPy import NeuroPy
from classifier import Classifier
from NK_Interface import NK_Interface
from trainingSets import *
import Tkinter
#import gui class here
import time, sys


def main(argv):
    #start gui to train
    trainingSet1 = [0,1,2,3,2,1,3,0,2,1,0,3,0,3,2,1,3,2,0,1]
    gui = NK_Interface(0,1,1, dir_list)
    gui.init_calib()
    rawData = gui.return_data()

    #gui takes up a lot of ram delete it
    del gui

    #create feature vectors
    c = Classifier(False)
    trainingData = []
    for a in rawData:
        trainingData.append(c.createFeatureVector(a[0], a[1]))

    #train classifier

    data = c.train(trainingData)
    for d in data:
        print d
    # run function from driver that send key commands to the system





if __name__ == "__main__":
   main(sys.argv[1:])
