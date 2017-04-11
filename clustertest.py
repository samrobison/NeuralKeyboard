from classifier import Classifier
from testData import *

c = Classifier(False)
trainingData = []
for a in rawData:
    trainingData.append(c.createFeatureVector(a[0], a[1]))

#train classifier

repeat = True
data = []
clusters = 7 

for k in range(20):
    c = Classifier(False)

    if repeat == False:
        continue

    data = c.train(trainingData,clusters)

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
    else:
        #clean training data
        for i in trainingData:
            del i[-1]

if repeat == True:
    print("Calibration Failed Please Repeat")
else:
    print("Calibration Successful")
