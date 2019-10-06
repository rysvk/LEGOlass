import math

class Color(object):
    
    def __init__(self, red, green, blue):
        self.red = int(red)
        self.green = int(green)
        self.blue = int(blue)

    @staticmethod
    def fromRGBTuple(tuple):
        return Color(tuple[0],tuple[1],tuple[2])

    def distance(self, color):
        rmean = ( self.red + color.red ) / 2;
        r = self.red - color.red;
        g = self.green - color.green;
        b = self.blue - color.blue;
        return math.sqrt((((512+rmean)*r*r)>>8) + 4*g*g + (((767-rmean)*b*b)>>8));
        # Do not use euclidian distance
        # https://en.wikipedia.org/wiki/Color_difference#CIELAB_%CE%94E*
        # https://stackoverflow.com/questions/9018016/how-to-compare-two-colors-for-similarity-difference
        #return (self.red-color.red)**2 + (self.green-color.green)**2 + (self.blue-color.blue)**2

    def closest(self, colors):
        minDev = self.distance(colors[0])
        min=0
        for i in range(1,len(colors)):
            dev=self.distance(colors[i])
            if(dev<minDev):
                min=i
                minDev=dev
        return colors[min]
