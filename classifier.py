import csv
import pandas as pd
import numpy as np
import numpy.fft

from clustering import kmeans
from clustering import fitNewPoint

class Classifier:
    def __init__(self, fileName):
        if fileName != False:
            self.data = pd.read_csv(fileName)
        self.fileName = fileName
        self.epslion = .1

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

        #power spectral density
        P = abs(numpy.fft.fft(data))
        for i in P:
            i = i ** 2
        P = sum(P)
        reducedData.append(float(P))

        #spectral entropy
        d = P/(P + 1e-12)
        logd = np.log2(d + 1e-12)
        ent = -1*((d*logd)/np.log2(2))
        #reducedData.append(float(ent))

        #std
        std = np.std(np.array(data))

        #normalize feature vector
        reducedData = np.array(reducedData)
        norm = (reducedData - reducedData.mean())/ reducedData.std()

        reducedData = norm.tolist()

        #add label
        reducedData.append(label)
        return reducedData


    def addTrainingData(self, data):
        with open('./train.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow(data)

    def train(self, data):
        if self.fileName != False:
            self.data = pd.read_csv('./train.csv')
        #normalize
        #norm = (data - data.mean())/ data.std()
        clusteredData , self.clusters = kmeans(4, data)
        return clusteredData

    def fitData(self, data):
        return fitNewPoint(self.centroids, data, self.epsilon)

    def saveTrainingData(self):
        with open('./train.csv', 'ab') as f:
            writer = csv.writer(f)
            for i in self.data:
                writer.writerow(i)
