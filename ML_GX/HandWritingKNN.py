import os
import numpy as np


def img2Vector(filename):
    Vect = np.zeros((1, 1024))
    f = open(filename, 'r')
    lines = f.readlines()
    line_num = len(lines)
    for i in range(line_num):
        oneLine = lines[i].strip()
        n = len(oneLine)
        if not n:
            continue
        for j in range(n):
            Vect[0,i*n+j] = int(oneLine[j])
    f.close()
    return (Vect)

def loadDataset(filedir):
    dataLists = os.listdir(filedir)
    num = len(dataLists)
    set_X = np.zeros((num, 1024))
    print("the shape of the dataset is:", np.shape(set_X))
    set_Y = []

    for i in range(num):
        filename = dataLists[i]
        label_i = int(filename.split('_')[0])
        set_Y.append(label_i)
        oneSample = img2Vector(filedir +'/' + filename)
        set_X[i,:] = oneSample
    return set_X, set_Y

def HandWritingTest(train_X, train_y, test_X, test_y, k):

    # guess_y = []

    testNum = len(test_X )
    trainNum = len(train_X)
    acc = 0.
    for i in range(testNum):
        if i %100 ==0:
            print("Calculating test:", i)
        testArray = np.tile(test_X[i], (trainNum, 1))

        # 计算每一个test_X中的元素与train_X的欧氏距离，并从小到大排序
        dis = ( np.sum((testArray - train_X) **2, axis=1)) **0.5
        Dis = np.argsort(dis)

        # 取得前K个最近元素
        vote = {}

        for j in range(k):
            # print("what j in k:", j)
            labels = train_y[Dis[j]]
            # print("labels in  lap:", labels)
            vote[labels] = vote.get(labels, 0) + 1
        sortVote = sorted(vote.items(), key=lambda x:x[1], reverse=True)
        testValue = test_y[i]
        #累加判断不正确的数量
        guess_y = sortVote[0][0]
        if guess_y != test_y[i]:
            acc +=1
    #计算错误率
    print ("acc is:", acc)
    acc = (testNum-acc)/testNum
    print("trainNum:",trainNum)
    return acc








train_X, train_Y = loadDataset('/home/getfox/GX_Files/ML/MachineLearning/KNN/data/trainingDigits')
test_X, test_Y = loadDataset('/home/getfox/GX_Files/ML/MachineLearning/KNN/data/testDigits')
# k = int(input("input K:"))
accuracy = HandWritingTest(train_X, train_Y, test_X, test_Y, k=7)
print("the KNN method can reach the accuracy:", accuracy)














