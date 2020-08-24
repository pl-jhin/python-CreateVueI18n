# encoding:utf-8
import urllib.request
import urllib.parse
import json
import random
import hashlib
import operationFile
import time
# 文件目录
dataPath = r"/Users/penglei/PycharmProjects/CreateVuei18n/createVuei18n/js/html-label.js"
# 导出文件目录
savePath = r"/Users/penglei/PycharmProjects/CreateVuei18n/createVuei18n/js/html-label-en.js"

def fanyiDict(labelJson):
    index = 1
    for data in labelJson:
        if isinstance(labelJson[data], dict):
            for k in labelJson[data]:
                print("第" + str(index) + "个")
                print("开始翻译值" + labelJson[data][k])
                en = youdao_translate(labelJson[data][k])
                print("翻译成功，结果为" + en)
                # time.sleep(1)
                labelJson[data][k] = en
            bJson = json.dumps(labelJson, ensure_ascii=False, sort_keys=True, indent=2)
    return bJson



def main():
    html = operationFile.readHTML(dataPath)
    labelJson = json.loads(html)
    bJson = fanyiDict(labelJson)
    # 写入文件
    operationFile.write(bJson, savePath)


def youdao_translate(content):
    key = content
    ts = str(time.time() * 1000)
    salt = ts + str(random.randint(1, 10))
    sign = hashlib.md5(('fanyideskweb' + key + salt + 'Nw(nmmbP%A-r6U3EUn]Aj').encode('utf-8')).hexdigest()
    '''有道翻译'''
    youdao_url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    data = {}
    # 调接口时所需参数，看自己情况修改，不改也可调用
    data['i'] = content
    data['from'] = 'AUTO'
    data['to'] = 'AUTO'
    data['smartresult'] = 'dict'
    data['client'] = 'fanyideskweb'
    data['salt'] = salt
    data['sign'] = sign
    data['doctype'] = 'json'
    data['version'] = '2.1'
    data['keyfrom'] = 'fanyi.web'
    data['action'] = 'FY_BY_CLICKBUTTION'
    data['typoResult'] = 'false'
    data = urllib.parse.urlencode(data).encode('utf-8')
    # 发送翻译请求
    youdao_response = urllib.request.urlopen(youdao_url, data)
    # 获得响应
    youdao_html = youdao_response.read().decode('utf-8')
    target = json.loads(youdao_html)
    # 取出需要的数据
    trans = target['translateResult']
    ret = ''
    for i in range(len(trans)):
        line = ''
        for j in range(len(trans[i])):
            line = trans[i][j]['tgt']
        ret = line
    return ret


if __name__ == '__main__':
    main()
