#读取文件demo

def readFile(filePath,type):
    """
    读取文件
    :param filePath: 文件路径
    :param type: r-读 w-写（每次写之前会清空原来文件里面的东西） a-追加（会保留原来文件里的东西） b-读取二进制文件（音频视频等）+ -读写模式
    :return:
    """
    try:
        with open(filePath,type,encoding='GBK') as fileObj:
            #line=fileObj.read()
            while True:
                line=fileObj.readline()
                print(line)

    except Exception as e:
        print('file not exist!'+e)

#调用方法
filePath='C:\\Users\\hadoop\\Desktop\\readme.txt'
readFile(filePath,'r')