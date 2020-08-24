# coding:utf-8
import operationFile
from textCommon import operationText
import json
import re

jsonPath = r"C:\Users\Administrator\PycharmProjects\pythonProject\HotentTools\front\label.js"
pathRoot = r'C:\Users\Administrator\Desktop\frontCopy\src'

def myprint(d):
    for k, v in d.items():
        if isinstance(v, dict):
            myprint(v)
        else:
            print("{0} : {1}".format(k, v))


def openJSON(jsonPath):
    # 获得json文件
    jsonScript = open(jsonPath, 'r', encoding="UTF-8").read()
    return jsonScript


def openOneFormat(jsonScript):
    # 转换json文件
    json_data = json.loads(jsonScript)
    fileNameList = operationFile.getFileName(pathRoot)
    for fileName in fileNameList:
        # 获得文本
        html = operationFile.readHTML(fileName)
        # 提取全部中文信息
        # datas = operationText.getScript(html)
        fileBaseName = operationText.getJsonName(fileName)
        print("开始操作文件名为" + fileBaseName)
        for key in json_data:
            str1 = "label=\"" + json_data[key] + "\""
            str2 = "label=\'" + json_data[key] + "\'"
            str3 = ":label=\"$t('label." + key + "')" + "\""
            print("开始将---" + str1 + "\n替换为---" + str3)
            print("开始将---" + str2 + "\n替换为---" + str3)
            html = re.sub(str1, str3, html)
            html = re.sub(str2, str3, html)
            operationFile.write(html, fileName)
    # print(html)


def opensFormatAll(jsonScript):
    # 转换json文件
    json_data = json.loads(jsonScript)
    fileNameList = operationFile.getFileName(pathRoot)
    for fileName in fileNameList:
        # 获得文本
        html = operationFile.readHTML(fileName)
        # 提取全部中文信息
        # datas = operationText.getScript(html)
        fileBaseName = operationText.getJsonName(fileName)
        # print("开始操作文件名为" + fileBaseName)
        for jsonData in json_data[fileBaseName]:
            text = json_data[fileBaseName][jsonData]
            str1 = text + "<"
            str2 = "{{$t('eip." + fileBaseName + "." + jsonData + "')}}" + "<"
            print("开始将---" + str1 + "\n替换为---" + str2)
            html = re.sub(str1, str2, html)
            # operationFile.write(html,fileName)


def main():
    # 获得json文件
    jsonScript = openJSON(jsonPath)
    openOneFormat(jsonScript)


if __name__ == '__main__':
    main()
