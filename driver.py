#!/usr/bin/python

from NeuroPy import NeuroPy
from classifier import Classifier
from NK_Interface import NK_Interface
from trainingSets import *
import Tkinter
#import gui class here
import time, sys
from time import *
from NeuroPy import NeuroPy
from clustertest import testCalibration
from MovingCircle import *


def callBackFunc(val):
    if takeData != False:
        takeData.append(val)


def main(argv):
    colors = 0
    sound = 0
    delay = 1
    #start gui to train
    gui = NK_Interface(colors,sound ,delay, trainingSet1)
    gui.init_calib()
    rawData = gui.return_data()

    #gui takes up a lot of ram delete it
    del gui

    # gui = NK_Interface(colors,sound,delay, trainingSet2)
    # gui.init_calib()
    # rawData += gui.return_data()
    #
    # del gui
    # print rawData
    #create feature vectors
    c = Classifier(False)
    trainingData, avg,std = c.createFeatureVectorTrain(rawData)

    #train classifier
    pack = testCalibration(trainingData)
    data = pack[0]
    centroids = pack[1]
    epsilon = pack[2]
    labels = pack[3]

    global takeData
    takeData= False
    # run function from driver that send key commands to the system
    mindWave = NeuroPy("/dev/tty.MindWaveMobile-DevA", 57600)
    mindWave.start()

    #start call back
    mindWave.setCallBack("rawValue", callBackFunc)

    g = Game()
    sleep(2)
    g.moveThing(0)
    sleep(1)

    g.moveThing(3)
    sleep(1)

    while True:
        g.resetPosition()
        takeData = []
        sleep(2)
        predict = takeData[:]
        takeData = False
        predict = c.createFeatureVectorFit(predict, avg, std)
        direction = c.predict( predict,centroids, epsilon)
        if direction != -1:
            print labels[direction]
            if labels[direction] == 'up':
                g.moveThing(0)
            elif labels[direction] == 'right':
                g.moveThing(1)
            elif labels[direction] == 'down':
                g.moveThing(2)
            elif labels[direction] == 'left':
                g.moveThing(3)
            sleep(.5)
        else:
            print "noise"








if __name__ == "__main__":
   main(sys.argv[1:])
