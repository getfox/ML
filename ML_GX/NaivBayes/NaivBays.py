
# 使用朴素贝叶斯方法判断敏感文字

from numpy import *

def loadDataset():
    postingList=[['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
                 ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                 ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                 ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                 ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                 ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classVec = [0,1,0,1,0,1]    #1 is abusive, 0 not
    return postingList,classVec

# 创建一个字典，根据标签存储单词

def volList(dictList, listLabel):
    abuseWords = []                                 # abuseWords 就是打了标签1的Vocabulary，根据标签分类
    normalWords = []                                # normalWords 就是打了标签0的Vocabulary，根据标签分类
    abuseDict = {}
    normalDict = {}

    labels = listLabel
    for i in range(len(labels)):
        if labels[i] == 1:
            abuseWords = abuseWords | dictList[i]   # 先把abuse words提取出来形成一个set
        else:
            normalWords = normalWords | dictList[i] # 再把normal words提取出来形成一个set
    abuseDict[abuseWords] = abuseDict.get(abuseWords, 0) + 1             # 再把set里的元素累加到Dict里并计数
    normalDict[normalWords] = normalDict.get(normalWords, 0) + 1             # 再把set里的元素累加到Dict里并计数
    return abuseDict, normalDict

def pInput(numInput, numTotal):             # 输入词占整体比率
    return float(numInput/numTotal)

def pAbuse(numAbuse, numTotal):             # 敏感词占整体比率
    return float(numAbuse/numTotal)

def pInputOnAbuse(numInput, numAbuse):      # 条件概率P（Input|Abuse）
    return float(numInput/numAbuse)

def NaivBayes():                            # 计算P(Abuse|Input) = P(Input|Abuse)P(Abuse)/P(Input) 和 P(Normal|Input)
    testDataset = ['my', 'love', 'dalmation']
    postingList, classVec = loadDataset()
    abuDict, norDict = volList(postingList, classVec)

    numInput = len(testDataset)
    numTotal = len(postingList)
    numAbuse = len(abuDict)
    numNormal = len(norDict)

    pAI = pInputOnAbuse(numInput, numAbuse) * pAbuse(numAbuse, numTotal) / pInput(numInput, numTotal)
    pNI = pInputOnAbuse(numInput, numNormal) * pAbuse(numAbuse, numTotal) / pInput(numInput, numTotal)

    if pAI > pNI:
        print("We predict the words %s is ABUSED." % testDataset)
    else:
        print("We predict the words %s is normal." % testDataset)
    return 0

NaivBayes()



