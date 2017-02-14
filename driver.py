#!/usr/bin/python

from NeuroPy import NeuroPy
from classifier import Classifier
#import gui class here
import time, sys


def main(argv):
    #start mindWave
    c = Classifier()
    #start gui with instance of Classifier
    #close gui after training data is added
    #train our classifier

    c.train()
    # run function from driver that send key commands to the system





if __name__ == "__main__":
   main(sys.argv[1:])
