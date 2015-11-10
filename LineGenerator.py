#coding=utf-8
'''
负责处理各种形式的输入，并逐行产生输出
'''
import sys
class LineGenFromFile(object):
    def __init__(self,filePath):
        '''
        根据文件路径初始化
        路径必须为文件的完整路径
        :param filePath:
        :return:
        '''
        self.filePath=filePath

    def generateLine(self):
        #print u'文件路径%s'%(self.filePath)
        with open(self.filePath,'rb') as f:
            for line in f.readlines():
                yield line.strip()

class LineGenFromStdIn(object):
    def generateLine(self):
        #print u'输入文本，win下面的Ctrl+Z, *nix下的Ctrl+d为结束符'
        for line in sys.stdin:
            yield line.strip()

class LineGenFromSocket(object):
    def generateLine(self):
        pass

if __name__=="__main__":
    tmp=LineGenFromStdIn()
    for line in tmp.generateLine():
        print u'经过生成器生成的一行%s'%line