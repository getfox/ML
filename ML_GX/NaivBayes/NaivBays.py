
# 使用朴素贝叶斯方法判断敏感文字

# from numpy import *

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
    abuseDict = {}
    normalDict = {}

    labels = listLabel
    for i in range(len(labels)):
        if labels[i] == 1:
            for j in range(len(dictList[i])):
                abuseDict[dictList[i][j]] = abuseDict.get(dictList[i][j], 0) + 1 # 把abusive words录入一个字典并统计每个单词出现的次数
        elif labels[i] == 0:
            for j in range(len(dictList[i])):
                normalDict[dictList[i][j]] = normalDict.get(dictList[i][j], 0) + 1 # 把normal words录入一个字典并统计每个单词出现的次数

    return abuseDict, normalDict

def pInput(numInput, numTotal):             # 输入词占整体比率
    return float(numInput/numTotal)

def pAbuse(numAbuse, numTotal):             # 敏感词占整体比率
    return float(numAbuse/numTotal)

# 计算条件概率P（Input|Condition）就是统计testDataset里面的词出现在conditionDict字典里的次数
def pInputOnCondition(testDataset, conditionDict):
    num = 0
    m = len(testDataset)
    for i in range(m):
        num = conditionDict.get(testDataset[i], 0) + 1
    num /=sum(conditionDict.values())
    return num
# 计算P(Abuse|Input) = P(Input|Abuse)P(Abuse)/P(Input) 和 P(Normal|Input)
def NaivBayes():
    testDataset = ['my', 'love', 'dalmation']
    postingList, classVec = loadDataset()
    abuDict, norDict = volList(postingList, classVec)

    numInput = len(testDataset)
    numAbuse = sum(int(i) for i in abuDict.values())
    numNormal = sum(int(i) for i in norDict.values())
    numTotal = numAbuse + numNormal

    pAI = pInputOnCondition(testDataset, abuDict) * pAbuse(numAbuse, numTotal)
    pNI = pInputOnCondition(testDataset, norDict) * pAbuse(numNormal, numTotal)

    if pAI > pNI:
        print("We predict the words %s is ABUSED." % testDataset)
    else:
        print("We predict the words %s is normal." % testDataset)
    return 0
if __name__ == '__main__':
    NaivBayes()



