import csv
import pandas as pd
from clustering import kmeans
from clustering import fitNewPoint

class Classifier:
    def __init__(self):
        self.data = pd.read_csv('./train.csv')
        self.epslion = .1

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
