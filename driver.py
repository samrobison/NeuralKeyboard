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


def callBackFunc(val):
    if takeData != False:
        takeData.append(val)


def testCalibration(rawData):
    c = Classifier(False)
    trainingData = []
    for a in rawData:
        trainingData.append(c.createFeatureVector(a[0], a[1]))

    repeat = True
    data = []


    for k in range(20):

        clusters = 6
        c = Classifier(False)
        data = c.train(trainingData, clusters)

        for d in data:
            print d

        count = []
        for i in range(clusters):
            count.append([])

        for i in data:
          count[i[-1]].append(i[len(i)-2])


        cou = 0
        cs = []
        for l in count:
            cs.append(max(set(l), key=l.count))
            print(str(cou)+". "+str(max(set(l), key=l.count)))
            cou += 1

        if "up" in cs and "right" in cs and "left" in cs and "down" in cs:
            print count
            repeat = False
            print("Calibration Successful")
            return cs, c

        else:
            #clean training data
            for i in trainingData:
                del i[-1]


    if repeat == True:
        print("Calibration Failed\nClosing Program")
        sys.exit()


def main(argv):
    colors = 1
    sounds = 0
    delay = 1
    #start gui to train
    gui = NK_Interface(color,sound ,delay, trainingSet1)
    gui.init_calib()
    rawData = gui.return_data()

    #gui takes up a lot of ram delete it
    del gui

    gui = NK_Interface(color,sound,delay, trainingSet2)
    gui.init_calib()
    rawData += gui.return_data()

    del gui
    print rawData
    #create feature vectors
    c = Classifier(False)
    trainingData = []
    for a in rawData:
        trainingData.append(c.createFeatureVector(a[0], a[1]))

    #train classifier
    labels, c = testCalibration(rawData)


    global takeData
    takeData= False
    # run function from driver that send key commands to the system
    mindWave = NeuroPy("/dev/tty.MindWaveMobile-DevA", 57600)
    mindWave.start()

    #start call back
    mindWave.setCallBack("rawValue", callBackFunc)

    print c.epsilon
    while True:
        takeData = []
        sleep(2)
        predict = takeData[:]
        takeData = False
        predict = c.createFeatureVector(predict, False)
        direction = c.predict(predict)
        if direction != -1:
            print labels[direction]
        else:
            print "noise"








if __name__ == "__main__":
   main(sys.argv[1:])
