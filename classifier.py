import csv
import pandas as pd
import numpy as np
import numpy.fft

from clustering import kmeans
from clustering import fitNewPoint
from clustering import calculateEpsilon
from pyeeg      import *

class Classifier:
    def __init__(self, fileName):
        if fileName != False:
            self.data = pd.read_csv(fileName)
        self.fileName = fileName
        self.epsilon = 0

    def createFeatureVector(self, data, label):
        #clone and remove label

        reducedData = []
        #max
        reducedData.append(float(max(data)))

        #min
        reducedData.append(float(min(data)))

        #mean
        avg = np.mean(np.array(data))
        reducedData.append(float(avg))

        #median
        median = np.median(np.array(data))
        reducedData.append(float(median))

        #rms
        rms = 0
        for i in data:
            rms += i**2
        rms = rms ** .5
        reducedData.append(rms)

        #std
        std = np.std(np.array(data))

        #power
        b = bin_power(data, [0.5,4,7,12,30], len(data)/2)
        for i in b[1]:
            reducedData.append(float(i))

        #spectral entropy
        spec = spectral_entropy(data,[0.5,4,7,12,30],len(data)/2,Power_Ratio = b[1])


        #normalize feature vector
        reducedData = np.array(reducedData)
        norm = (reducedData - reducedData.mean())/ reducedData.std()

        reducedData = norm.tolist()

        #add label
        if label != False:
            reducedData.append(label)
        return reducedData


    def addTrainingData(self, data):
        with open('./train.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow(data)

    def train(self, data, clusters):
        if self.fileName != False:
            self.data = pd.read_csv('./train.csv')
        #normalize
        #norm = (data - data.mean())/ data.std()
        clone = list(data)
        clusteredData , self.centroids = kmeans(clusters, clone)
        self.epsilon = calculateEpsilon(clusteredData, self.centroids)
        print "Eplison is: " + str(self.epsilon)
        return clusteredData

    def predict(self, data):
        return fitNewPoint(self.centroids, data, 99999.999)

    def saveTrainingData(self):
        with open('./train.csv', 'ab') as f:
            writer = csv.writer(f)
            for i in self.data:
                writer.writerow(i)
