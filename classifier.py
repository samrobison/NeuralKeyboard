import csv
import pandas as pd
import numpy as np
import numpy.fft

from clustering import kmeans
from clustering import fitNewPoint
from clustering import calculateEpsilon

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

        # #power spectral density
        # P = abs(numpy.fft.fft(data))
        # for i in P:
        #     i = i ** 2
        # P = sum(P)
        # reducedData.append(float(P))
        #
        # #spectral entropy
        # d = P/(P + 1e-12)
        # logd = np.log2(d + 1e-12)
        # ent = -1*((d*logd)/np.log2(2))
        # reducedData.append(float(ent))

        #rms
        rms = 0
        for i in data:
            rms += i**2
        rms = rms ** .5
        reducedData.append(rms)

        #std
        std = np.std(np.array(data))

        #number of 0 crossings
        lastPos = data[0] > 0
        count = 0
        for i in data:
            if lastPos and i < 0:
                count += 1
            elif not lastPos and i > 0:
                count += 1
            lastPos = i > 0
        reducedData.append(count)

        #rise time to peak
        peakIndex = data.index(max(data))
        freq = 2.0/len(data)
        riseTime = (peakIndex+1) * freq
        reducedData.append(riseTime)


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
