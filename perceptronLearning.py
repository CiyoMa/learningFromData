import random
from numpy import zeros

def dot(l,m):
    assert len(l) == len(m)
    return sum([l[i] * m[i] for i in range(len(l))])

def getParameters(trainMatrix, trainLabels, iterationLimit = 10000):
    theta = zeros(len(trainMatrix[0]))
    iteration = 1
    while True:
        flag = True
        mistake = 0
        for i in range(len(trainMatrix)):
            # print trainMatrix[i], trainLabels[i]
            test = [t * trainLabels[i] for t in trainMatrix[i]]
            # print '===!'
            # print test
            # print test, theta
            value = dot(test,theta)
            # print '!'
            if value <= 0:
                mistake += 1
                theta = [theta[j]+test[j] for j in range(len(theta))]
                flag = False
                break
        # print "iteration", iteration, ":", mistake, "mistakes"
        iteration += 1
        if flag or iterationLimit < iteration:
            break

    return iteration, [i for i in theta]

def targetFunction(xy0,xy1,x,y):
    x0 , y0 = xy0
    x1 , y1 = xy1
    if (x1-x0)*(y-y0) - (y1-y0)*(x-x0) >= 0:
        return 1
    return -1

def generateData(numSamples):
    x0 = random.uniform(-1,1)
    y0 = random.uniform(-1,1)
    x1 = random.uniform(-1,1)
    y1 = random.uniform(-1,1)
    xy0 = (x0, y0)
    xy1 = (x1, y1)
    points = []
    for i in range(numSamples):
        x, y =random.uniform(-1,1), random.uniform(-1,1)
        points.append( ([1, x, y], targetFunction(xy0,xy1,x,y)) )
    # for p in points:
    #     print p
    return xy0, xy1, points

def oneTrial(numSamples):
    xy0, xy1, points = generateData(numSamples)
    trainMatrix = [p[0] for p in points]
    trainLabels = [p[1] for p in points]
    iterations, theta = getParameters(trainMatrix, trainLabels)
    return iterations, disagreementRate(theta, xy0, xy1)

def disagreementRate(weight, xy0, xy1):
    def sign(x):
        if x>=0:
            return 1
        return -1

    x0, y0 = xy0
    x1, y1 = xy1
    numTests = 1000
    mistakes = 0
    for i in range(numTests):
        # print '----------'
        x, y = random.uniform(-1,1), random.uniform(-1,1)
        # print '!!'
        f = weight[0] + dot(weight[1:], [x, y])
        if sign(f) != targetFunction(xy0, xy1, x, y):
            mistakes += 1
    return mistakes / 1000.0

#######################################################################
# Main
#######################################################################

def main():
    numSamples = 10
    iterations = []
    errors = []
    for i in range(1000):
        it, err = oneTrial(numSamples)
        iterations.append(it)
        errors.append(err)
    print sum(iterations) / 1000.0
    print sum(errors) / 1000.0  


if __name__ == '__main__':
    main()