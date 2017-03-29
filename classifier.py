import csv
import pandas as pd
import numpy
from clustering import kmeans
from clustering import fitNewPoint

class Classifier:
    def __init__(self):
        #self.data = pd.read_csv('./train.csv')
        self.epslion = .1

    def reduceData(oldData):
        #clone and remove label
        data = oldData[:]
        del data[-1]

        reducedData = []
        #means
        for i in data:
            avg = numpy.mean(numpy.array(a))
            reducedData.append(avg)
        #medians
        for i in data:
            median = numpy.median(numpy.array(lst))
            reducedData.append(median)
        #spectral energy sum of all k(n)*log(k(n))
        for i in data:
            spectralEnergy = 0
            for k in i:
                spectralEnergy += (k * numpy.log(k))
            reducedData.append(spectralEnergy)
        #spectralEntropy



    def addTrainingData(data):
        with open('./train.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow(data)

    def trainClassifier():
        self.data = pd.read_csv('./train.csv')
        #normalize
        norm = (data - data.mean())/ data.std()
        clusteredData , self.clusters = kmeans(3, norm.values.tolist())

    def fitData(data):
        return fitNewPoint(self.centroids, data, self.epsilon)

    def saveTrainingData():
        with open('./train.csv', 'ab') as f:
            writer = csv.writer(f)
            for i in self.data:
                writer.writerow(i)
