from classifier import Classifier
from testData import *
from sklearn.decomposition import PCA

def testCalibration(trainingData):
    c = Classifier(False)
    #print trainingData

    #train classifier

    data = []
    clusters = 8

    bestclustered = []
    bestCentroids = []
    bestavg = 0.0
    bestcs = []
    bestcount = []
    for k in range(200):
        c = Classifier(False)

        pack = c.train(trainingData,clusters)
        data = pack[0]
        centroids = pack[1]
        epsilon = pack[2]
        if data == False:
            for i in trainingData:
                del i[-1]
            continue

        # for d in data:
        #     print d

        count = []
        for i in range(clusters):
            count.append([])

        for i in data:
          count[i[-1]].append(i[len(i)-2])

        cou = 0
        cs = []
        for l in count:
            cs.append(max(set(l), key=l.count))
            #print(str(cou)+". "+str(max(set(l), key=l.count)))
            cou += 1


        if "up" in cs and "right" in cs and "left" in cs and "down" in cs:
            avgcorrect = 0
            for i in range(len(count)):
                correct = 0.0
                for k in count[i]:
                    if k == cs[i]:
                        correct += 1.0
                avgcorrect += float(correct/ len(count[i]))
            avgcorrect /= len(cs)
            #print avgcorrect
            if avgcorrect > bestavg:
                bestCentroids = centroids
                bestclustered = data
                bestavg = avgcorrect
                bestcs = cs
                bestcount = count
            #clean training data
        for i in trainingData:
            del i[-1]
    print " --------------------"
    print bestavg
    print bestcount

    if bestavg == 0.0:
        print("Calibration Failed Please Repeat")
    else:
        print("Calibration Successful")
        return (bestclustered, bestCentroids, 99999.999, bestcs)


#testCalibration(testrawdata)
