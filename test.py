#coding=utf-8
'''

'''
import os
from WorldHandle import FileInOut
#a=FileInOut('./InFile','./tmp')
#a.handle()
def mainFoo():
    '''
    程序入口
    :return:
    '''
    inFilePath=raw_input(u'In file path:')
    while not os.path.isdir(inFilePath):
        inFilePath=raw_input(u'illegal path , try again:')
    inFileName=raw_input(u'In file name:')
    inFile=os.path.join(inFilePath,inFileName)
    while not os.path.isfile(inFile):
        inFileName=raw_input(u'illegal file , try again:')
        inFile=os.path.join(inFilePath,inFileName)

    outFilePath=raw_input(u'Out file path')
    while not os.path.isdir(outFilePath):
        outFilePath=raw_input(u'illegal path , try again:')
    outFileName=raw_input(u'In file name:')
    outFile=os.path.join(outFilePath,outFileName)

    a=FileInOut(inFile,outFile)
    a.handle()

if __name__=="__main__":
    mainFoo()