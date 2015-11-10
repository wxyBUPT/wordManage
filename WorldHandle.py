#coding=utf-8
'''
实现文本处理逻辑，根据单行生成器产生输出结果
'''
from LineGenerator import LineGenFromStdIn,LineGenFromFile
from LineReverse import LineReverse
class WorldHandle(object):
    def __init__(self,lineGenerator):
        self.lineGenerator=lineGenerator
    def generateRes(self):
        '''
        接收一个生成器作为参数
        :param lineGenerator:产生输入行的一个生成器
        :return:
        '''
        for line in self.lineGenerator:
            lineReverse=LineReverse(line)
            for lineRes in lineReverse.getOutPut():
                yield lineRes

class FileInOut(object):
    '''
    根据输入的文件和输出文件的完整路径完成逻辑
    '''
    def __init__(self,inFile,outFile):
        self.inFile=inFile
        self.outFile=outFile
    def handle(self):
        tmp=LineGenFromFile(self.inFile)
        lineGenerator=tmp.generateLine()
        res=WorldHandle(lineGenerator)
        res=res.generateRes()
        with open(self.outFile,'wb') as f:
            #print type(res)
            for line in res:
                #print line
                f.write(line)
                f.write('\n')

if __name__=="__main__":
    a=LineGenFromStdIn()
    tmp=WorldHandle(a.generateLine())
    for line in tmp.generateRes():
        print line