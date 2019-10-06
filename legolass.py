from FileUtils import FileUtils
from Color import Color
from PIL import Image, ImageFilter
from Logger import Logger
import sys
import time
import math
import concurrent.futures

Log=Logger.Log
LegoColorsFileName = "colors_lego.csv"
FileName = "lego_toy.jpg"
BlockSize = 4

def processArguments():
    global FileName
    global BlockSize
    if(len(sys.argv)>1):
        FileName = str(sys.argv[1])
    if(len(sys.argv)>2 and sys.argv[2].isdigit()):
        BlockSize = int(sys.argv[2])

def legolass(image, blockSize):
    width = image.width
    height = image.height
    for i in range(int(math.ceil(width/blockSize)) + 1):
        for j in range(int(math.ceil(height/blockSize)) + 1):
            assignMeanClosestColor(image, i * blockSize, j * blockSize, blockSize)

def assignMeanClosestColor(image, startRow, startCol, gridWidth):
    redSum = greenSum = blueSum = 0
    count = 0
    for i in range(startRow, min(startRow + gridWidth, image.width)):
        for j in range(startCol, min(startCol + gridWidth, image.height)):
            red, green, blue = image.getpixel((i, j))
            redSum += red
            greenSum += green
            blueSum += blue
            count += 1
    if(count==0):
        return
    closestColor = Color(int(redSum/count), int(greenSum/count), int(blueSum/count)).closest(legoColors)
    for i in range(startRow, min(startRow + gridWidth, image.width)):
        for j in range(startCol, min(startCol + gridWidth, image.height)):
            image.putpixel((i, j),(closestColor.red, closestColor.green, closestColor.blue))

processArguments()
Log("****----- Loading Lego Colors -----****")
csvTuples = FileUtils.getCSVTuples(LegoColorsFileName)
legoColors = [Color.fromRGBTuple(csvTuple) for csvTuple in csvTuples]
Log("Total Colors Count : {}".format(len(legoColors)))
Log("===== Completed : Loading Lego Colors =====")
Log("****----- Loading Image : {} -----****".format(FileName))
inputImage = Image.open(FileName)
inputImage.show()
Log("===== Completed Loading Image : {}".format(FileName))

Log("****----- Legofying Image {}-----****".format(FileName))
now = time.time()
legolass(inputImage, BlockSize)
Log("time : {}".format(time.time()-now))
inputImage.show()
Log("****----- Completed : Legofying Image {}-----****".format(FileName))