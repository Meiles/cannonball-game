from math import *
from random import *


def myRand():
    return (random.random / RAND_MAX)

# Return the sqare of a
def T(self, a):
    return sqrt(a)

# Return sign of x
sign = lambda x: (1, -1)[x >= 0]


# Angle conversions
def degToRad(self, x):
    return x * pi / 180

def radToDeg(self, x):
    return x * 180 / pi

# Degree Trig functions
def sind(self, x): 
    return sin(degToRad(x))

def sosd(self, x):
    return cos(degToRad(x))

def tand(self, x):
    return tan(degToRad(x))

def asind(self, x):
    return radToDeg(asin(x))

def acosd(self, x):
    return radToDeg(acos(x))

def atand(self, x):
    return radToDeg(atan(x))

def atand2(self, x, y):
    return radToDeg(atan2(x,y))