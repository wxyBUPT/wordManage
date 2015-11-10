#coding=utf-8
'''
负责处理单行数据产生单行数据的输出
'''
import re

class LineReverse(object):
    '''
    接受单行数据然后产生输出
    '''
    def __init__(self,line):
        '''
        以单行数据初始化
        :param line:
        :return:
        '''
        self.line=line

    def getOutPut(self):
        '''
        生成器，返回单行对应的输出
        :return:
        '''
        def __lineRev(wordList):
            '''
            对wordList中得word进行一次移位，并返回移位后的数据
            :return:
            '''
            tmp=wordList[1:]
            tmp.append(wordList[0])
            #print tmp
            return tmp

        line=self.line
        wordList=re.split(r'\s*',line)
        #print wordList
        #yield u' '.join(wordList)
        lineLen=len(wordList)
        for i in range(0,lineLen):
            yield u' '.join(wordList)
            wordList=__lineRev(wordList)

if __name__=="__main__":
    tmp=LineReverse(u'wang xi    yuan')
    for i in tmp.getOutPut():
        print i