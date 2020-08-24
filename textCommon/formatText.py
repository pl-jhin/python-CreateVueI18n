# coding:utf-8

from textCommon import operationText

resultMapDict = {}


def getMap(list):
    # 第一次进入初始化
    resultMapDict = {}
    for data in list:
        # 格式化key
        dictKey = operationText.getStrAllAplha(data)
        dictKey = getNewKey(dictKey, resultMapDict)
        resultMapDict[dictKey] = data.replace(" ", "")
        resultMapDict[dictKey] = data
    return resultMapDict


def getNewKey(key, map):
    if key in map:
        print("存在重复的key=" + key)
        key = key + 'U'
        print("已将key替换为=" + key)
        return getNewKey(key, map)
    else:
        return key
