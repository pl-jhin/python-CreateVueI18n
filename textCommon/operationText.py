# coding:utf-8
import pinyin
import re
import os

# 策略类父类
class TextSuper:
    def getTextCN(self, label, html):
        pass

# 获得tags中文子类
class TagsCN(TextSuper):
    def getTextCN(self, tag, html):
        CNTexts = []
        resultList = []
        # 排除注解
        html = unNode(html)
        pat = r"<" + tag + r".*>.*</" + tag + ">"
        patSearch = r"<" + tag + r".*>(.*)</" + tag + ">"
        tagHtmls = re.findall(pat, html)
        for tagHtml in tagHtmls:
            CNHtmls = re.search(patSearch, tagHtml)
            if CNHtmls:
                flag = re.match(r'[\u4e00-\u9fa5]', CNHtmls.group(1))
                if flag:
                    CNTexts.append(CNHtmls.group(1))
        # 去重
        resultList = list(set(CNTexts))
        return resultList

# 获得labels中文子类
class LabelsCN(TextSuper):
    def getTextCN(self, label, html):
        CNTexts = []
        resultList = []
        # 排除注解
        html = unNode(html)
        pat = r'[^:]' + label + r'=[\"|\'][^\"]*[\"|\']'
        patSearch = r'[^:]' + label + r'=[\"|\']([^\"]*)[\"|\']'
        # 获得那整行
        labelHtmls = re.findall(pat, html)
        for labelHtml in labelHtmls:
            CNHtmls = re.search(patSearch, labelHtml)
            if CNHtmls:
                flag = re.match(r'[\u4e00-\u9fa5]', CNHtmls.group(1))
                if flag:
                    CNTexts.append(CNHtmls.group(1))
            # 去重
        resultList = list(set(CNTexts))
        return resultList

# 获得script中文子类
class ScriptCN(TextSuper):
    def getTextCN(self, script, html):
        CNList = []
        resultList = []
        # 排除注解
        html = unNode(html)
        scriptAllHtml = re.findall(r'<script>[\w\W]*<\/script>', html)
        pat = script + r'[:|\(|\'|\"|= ]+[^;|^)|^\"|^}|,]*[)|\"|\']'
        patSearch = script + r'[:|\(|\'|\"|=| ]+([^;|^)|^\"|^}|,]*)[)|\"|\']'
        for html in scriptAllHtml:
            scriptHtmls = re.findall(pat, html)
            for scriptHtml in scriptHtmls:
                CNHtmls = re.search(patSearch, scriptHtml)
                if CNHtmls:
                    flag = re.findall(r'[\u4e00-\u9fa5]', CNHtmls.group(1))
                    if flag:
                        CNList.append(CNHtmls.group(1))
            # 去重
        resultList = list(set(CNList))
        return resultList

# 上下文类
class Context:
    def __init__(self, text_super):
        self.text_super = text_super

    def GetJsonText(self, label, html):
        return self.text_super.getTextCN(self, label, html)


# 获得除注释外的全部中文
def getAllCN(html):
    resultList = []
    # 中文结果集
    CNList = []
    # 获得那整行
    tdData = re.findall(r"[\u4e00-\u9fa5，：]+<", html)
    for html in tdData:
        datas = re.search(r"([\u4e00-\u9fa5，：]+)<", html)
        if datas:
            data = datas.group(1)
            CNList.append(str(data))
            # 去重
            resultList = list(set(CNList))
    return resultList

# 排除注释
def unNode(html):
    unNotes = re.sub(r'//.*', "", html)
    unNotes = re.sub(r'/?\*.*\*/', "", unNotes)
    unNotes = re.sub(r"<!--.*-->", "", unNotes)
    return unNotes


# 获得大写拼音开头
def getStrAllAplha(str):
    jsonKey = ""
    Aplha = pinyin.get_initial(str, delimiter="").upper()
    jsonKeyList = re.findall(r'[A-Z]+', Aplha)
    for key in jsonKeyList:
        jsonKey += key
    return jsonKey


# 获得Json的Key
def getJsonName(filePath):
    fileName = os.path.basename(filePath)
    fileName = fileName.split('.')[0]
    return fileName
