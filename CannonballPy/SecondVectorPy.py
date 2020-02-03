from math import *
'''
x = 0.0
y = 0.0
z = 0.0
'''

class Vector3d:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        #self.test()

    def test(self):
        print('test')

    #copy constructor
    def __copy(self):
        return Vector3d(self.x, self.y, self.z)

    #addition
    def __add__(self, other):
        return Vector3d(self.x + other.x, self.y + other.y, self.z + other.z)

    #subtraction
    def __sub__(self, other):
        return Vector3d(self.x - other.x, self.y - other.y, self.z - other.z)

    #multiplication
    def __mul__(self, other):
        return Vector3d(self.x*other, self.y*other, self.z*other)

    '''
    #division
    def __div__(self, other):
        return self.__copy() * (other**-1)
        '''

    #equality
    def __eq__(self, other):
        return self.x == other.x, self.y == other.y, self.z == other.z

    #to string
    def __str__(self):
        return '(%s,%s,%s)' % (self.x,self.y,self.z)

    #negation
    def __neg__(self, other):
        return not self.__eq_(other)

    #cross product
    def __pow__(self, other):
        return Vector3d(self.y*other.z - self.z*other.y,
            self.z*other.x - self.x*other.z,
            self.other.y - self.y*other.x)

    #dot product
    def dot(self, other):
        temp = self * other
        return temp.x + temp.y + temp.z

    #magnitude
    def magnitude(self):
        return sqrt((self.x)^2 + (self.y)^2 + (self.z)^2)

    #normalize
    def normalize(self):
        return self.__copy() / self.magnitude()

    def GetX(self):
        return self.x

    def GetY(self):
        return self.y

    def GetZ(self):
        return self.z

    def SetX(self):
        self.x = x

    def SetY(self):
        self.y = y

    def SetZ(self):
        self.z = z

    def SetAll(self, d1, d2, d3):
        self.x = d1
        self.y = d2
        self.z = d3


if __name__ == '__main__':
    test = Vector3d(1,1,1)
    v1 = Vector3d(1,1,1)
    v2 = Vector3d(2,2,2)
    v3 = Vector3d(3,3,3)
    add = v1 + v2 + v3
    sub = v1 - v2
    #norm = Vector3d.normalize(v1)
    print(test)
    print(add)
    print(sub)
    #print(norm)




