# coding:utf-8
import os

listFileName = []
# 获得后缀是.vue的文件名
def getFileName(path):
    files = os.listdir(path)  # 获取当前目录的所有文件及文件夹
    for file in files:
        try:
            # 获取绝对路径
            file_path = os.path.join(path, file)
            # 判断是否是文件夹
            if os.path.isdir(file_path):
                # 如果是文件夹，就递归调用自己
                getFileName(file_path)
            else:
                extension_name = os.path.splitext(file_path)  # 将文件的绝对路径中的后缀名分离出来
                if extension_name[1] == '.vue':
                    listFileName.append(file_path)
        except:
            continue
    return listFileName

# 获得文本信息
def readHTML(fileName):
    html = open(fileName, 'r',encoding="utf-8").read()
    return html

def getFileTrueName(filePath):
    return os.path.basename(filePath).split('.')[0]


# 写入文件
def write(JsonResult,inputFilePath):
    f = open(inputFilePath, 'w',encoding="utf-8")
    f.write(JsonResult)
    f.close()