# coding:utf-8
# 导入模块
from fileCommon import operationFile
from textCommon import formatText
from textCommon.operationText import *

def getDatas(pathRoot, lists ,TextSuper):
    AllText = {}
    tagList = []
    fileNameList = operationFile.getFileName(pathRoot)
    print("一共有" + str(len(fileNameList)) + "个vue文件")
    for listData in lists:
        # 进入循环taglist清空
        tagList = []
        for fileName in fileNameList:
            # 获得文本
            html = operationFile.readHTML(fileName)
            # 根据不同的策略类调用不同的方法
            datas = Context(TextSuper).GetJsonText(listData,html)
            for data in datas:
                tagList.append(data)
            # 再次去重
        tagList = list(set(tagList))
        jsonMap = formatText.getMap(tagList)
        # 将jsonMap装箱
        AllText[listData] = jsonMap
    return AllText


