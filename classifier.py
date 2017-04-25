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

    def createFeatureVectorFit(self, data, avg, std):
        reducedData = []
        # #max
        # reducedData.append(float(max(data)))

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
        rms = (rms/len(data)) ** .5
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
        norm = np.array(reducedData)
        norm = (reducedData - avg)/ std

        reducedData = norm.tolist()
        return reducedData

        # #add label
        # if label != False:
        #     reducedData.append(label)
        # return reducedData

    def createFeatureVectorTrain(self, rawdata):

        featureVectors = []
        labels = []
        for d in rawdata:
            labels.append(d[-1])
            del d[-1]
            data = d[0]
            reducedData = []
            # #max
            # reducedData.append(float(max(data)))

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
            rms = (rms/len(data)) ** .5
            reducedData.append(rms)

            #std
            std = np.array(data).std

            #power
            b = bin_power(data, [0.5,4,7,12,30], len(data)/2)
            for i in b[1]:
                reducedData.append(float(i))

            #spectral entropy
            spec = spectral_entropy(data,[0.5,4,7,12,30],len(data)/2,Power_Ratio = b[1])
            reducedData.append(spec)
            featureVectors.append(reducedData)


        norm = np.array(featureVectors)
        avg = norm.mean()
        std = norm.std()
        norm = (featureVectors - avg)/ std

        featureVectors = norm.tolist()
        for i in range(len(featureVectors)):
            featureVectors[i].append(labels[i])

        return featureVectors, avg,std

    def addTrainingData(self, data):
        with open('./train.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow(data)

    def train(self, data, k):
        if self.fileName != False:
            self.data = pd.read_csv('./train.csv')
        clone = list(data)
        clusteredData , self.centroids = kmeans(k, clone)
        if clusteredData == False:
            return (False, False, False)
        self.epsilon = calculateEpsilon(clusteredData, self.centroids)
        print "Eplison is: " + str(self.epsilon)
        return (clusteredData, self.centroids, self.epsilon)

    def predict(self, data, cents, epsilon):
        return fitNewPoint(cents, data, 99999.999)

    def saveTrainingData(self):
        with open('./train.csv', 'ab') as f:
            writer = csv.writer(f)
            for i in self.data:
                writer.writerow(i)
