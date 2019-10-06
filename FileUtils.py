class FileUtils(object):
    
    @staticmethod
    def getLines(file, fileMode = 'r'):
        fileHandle =  open(file, fileMode)
        lines = fileHandle.readlines()
        fileHandle.close()
        lines = [line.strip() for line in lines ]
        return lines

    @staticmethod
    def getCSVTuples(file, fileMode= 'r'):
        lines = FileUtils.getLines(file, fileMode)
        csvTuples = [line.split(',') for line in lines]
        return csvTuples    