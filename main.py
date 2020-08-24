# coding:utf-8
# 导入模块
from fileCommon import operationFile
import json
from textCommon import getDatas
from textCommon.operationText import *

# 输出目录
outFilePath = r"/Users/penglei/PycharmProjects/CreateVuei18n/createVuei18n/js/html-label.js"
# 文件目录
pathRoot = r'/Users/penglei/Desktop/work/hotentWorkByHTML/web/manage'

# tags集合
tags = ['el-button', 'span', 'el-dropdown-item', 'th', 'el-tag' , 'th', 'td', 'label']

# labels集合
lables = ['placeholder', 'title', 'content', 'label']

# script集合
scripts = ['error','message','warning','success','value','title']

def main():
    # 传入集合和策略类
    resultMapDict = getDatas.getDatas(pathRoot, tags, TagsCN)
    bJson = json.dumps(resultMapDict, ensure_ascii=False, sort_keys=True, indent=2)
    # 写入文件
    operationFile.write(bJson, outFilePath)


if __name__ == '__main__':
    main()
