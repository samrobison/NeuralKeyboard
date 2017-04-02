import random
#from IPython import embed


def kmeans(n, data):
    #give all data points a place for cluster
    for i in data:
        i.append(0)
    #pick n points
    centroids = []
    randos = []
    #get starting points
    print "choosing centroids"
    for i in range(n):
        rand = int(random.random() * len(data))
        #make sure random centroid isn't taken
        while rand in randos:
            rand = int(random.random() * len(data))
        randos.append(rand)
    #assign starting points
    for i in randos:
        centroids.append(data[i])
    #500 times
    print "starting clustering"
    for i in range(500):
        #calculate each point's closest centroid
        for point in data:
            distances = []
            #calculate centroids distances
            for cent in centroids:
                distances.append(distance(point, cent))
            #assign cluster
            point[-1] = distances.index(min(distances))
        #recalculate centroids
        centroids = recalcCentroids(data, centroids)
    return data, centroids



def fitNewPoint(centroids, point, epsilon):
    distances = []
    for cent in centroids:
        distances.append(distance(point, cent))
    cluster = -1
    if distances.index(min(distances)) < epsilon:
        cluster = distances.index(min(distances))
    return cluster


def recalcCentroids(data, centroids):
    tmpCents = []
    for i in centroids:
        tmpCents.append([0] * len(centroids[0]))
    counts = [0] * len(centroids)

    for point in data:
        counts[point[-1]] += 1
        for i in range(len(point)):
            if point[i].__class__.__name__ == 'str':
                continue
            tmpCents[point[-1]][i] += point[i]
#    print counts
    for point in tmpCents:
        c = counts[tmpCents.index(point)]
        for k in range(len(point)):
            if point[k].__class__.__name__ == 'str':
                continue
            point[k] /= c
    return tmpCents

def clusterDistance(data, centroids):
    retVal = 0
    for point in data:
        retVal += distance(point, centroids[point[-1]])
    return retVal

def distance(p1, p2):
    dist = 0
    #1 less because of cluster place
    for i in range(len(p1)-1):
        if p1[i].__class__.__name__ == 'str' or p2[i].__class__.__name__ == 'str':
            continue
        dist += ((p2[i] - p1[i]) ** 2)
    return dist

def calculateEpsilon(data, centroids):
    maxDist = 0.0
    for i in data:
        dist = distance(i, centroids[i[-1]])
        if dist > maxDist:
            maxDist = dist
    return maxDist * 1.2

#might redefinine these later for our purposes but we don't need them as of now
# def miss(index, data):
#     #not the cleanest way but it seems to work
#     #take a consistant value from each class and use it to compare
#     if index < 60:
#         l = data[index][-1]
#         if l == data[30][-1]:
#             return True
#         else:
#             return False
#     else:
#         if index < 131:
#             if data[index][-1] == data[90][-1]:
#                 return True
#             else:
#                 return False
#         else:
#             if data[index][-1] == data[160][-1]:
#                 return True
#             else:
#                 return False
#
# def missCalced(index, data):
#     #same as other method but data is formatted slightly differently so it needs its own method
#     if index < 60:
#         l = data[index]
#         if l == data[30]:
#             return True
#         else:
#             return False
#     else:
#         if index < 131:
#             if data[index] == data[90]:
#                 return True
#             else:
#                 return False
#         else:
#             if data[index] == data[160]:
#                 return True
#             else:
#                 return False

def heirachrical(data, distanceMethod, n):
    #make each point a cluster
    clusters = []
    for point in data:
        clusters.append([point])
    while len(clusters) > n:
        #only thing that changes between methods is distance calculations
        p1,p2 = closestPoints(clusters, distanceMethod)
        #combine closest points
        clusters[p1] = clusters[p1] + clusters[p2]
        #deleted used cluster
        del clusters[p2]
    return clusters

def closestPoints(data, distanceMethod):
    # pointst that will be returned
    pair = [0,1]
    # ridiculous distance that wont happen
    dist = 999999999
    #ranges so that every point will be checked
    for i in range(len(data) -1) :
        for k in range(i+1, len(data)):
            #use selected distance method
            tmpDist = distanceMethod(data[i], data[k])
            #check for new minimum and update values
            if tmpDist < dist:
                dist = tmpDist
                pair = [i, k]
    return pair[0], pair[1]

#finds closest points between clusters
def closestInClusters(cluster1, cluster2):
    dist = 99999999
    for i in cluster1:
        for k in cluster2:
            tmpDist = distanceHC(i,k)
            if tmpDist < dist:
                dist = tmpDist
    return dist

#finds farthest points between clusters
def farthestInClusters(cluster1, cluster2):
    dist = -1
    for i in cluster1:
        for k in cluster2:
            tmpDist = distanceHC(i,k)
            if tmpDist > dist:
                dist = tmpDist
    return dist

def distanceHC(p1, p2):
    dist = 0
    for i in range(len(p1)):
        dist += ((p2[i] - p1[i]) ** 2)
    return dist
