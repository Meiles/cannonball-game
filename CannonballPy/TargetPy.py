from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from VectorPy import *
from BallPy import * # this is a place holder for the ball function
import sys
import random


damping = 0.95

collisionDamping = 0.3

class Target:
    center = Vector3d(0,0,0)
    color = Vector3d(255,0,0)
    _bbx = 0.
    innerRadius, outerRadius = 0., 0.
    isMoving = False
    deltaX = 0.
                            

    def __init__(self):
        center.SetAll(0,10,-80)
        color.SetAll(230,200,230)
        innerRadius = 0.5
        outerRadius = 4
        isMoving = False
        deltaX = 0.02

        #def SetRandomColor(self):

    def SetBBX(self, _bbx):
        self._bbx = _bbx

    def Update(self, ballList):
        if(isMoving):
            center.SetX(center.GetX() + deltaX)
            if(center.GetX() < _bbx[0]):
                center.SetX(_bbx[0])
                delta *= -1
            if(center.GetX() < _bbx[1]):
                center.SetX(_bbx[1])
                delta *= -1

        hit = False
        isLast = False
        curBall = Node()
        curBall = ballList
        while(curBall != None):
            b = Ball()
            setNext(b)
            b = curBall
            ballCenter = Vector3d(b.GetCenter())
            if((ballCenter-center).norm() < outerRadius):
                if(abs(ballCenter.GetZ()-center.GetZ()) < 1.0):
                    hit = True
                    break
            curBall = curBall.getNext()

        if(hit):
            isMoving = True

            color.SetX(random.random)
            color.SetY(random.random)
            color.SetZ(random.random)
            deltaX *= 1.05
    
    def Draw(self):
      #void glutSolidTorus(GLdouble innerRadius,
          #                  GLdouble outerRadius,
          #                  GLint nsides, GLint rings);

      glColor3f(color.GetX(),color.GetY(),color.GetZ())
      glPushMatrix()
      glTranslated(center[0],center[1],center[2])
      glutSolidTorus(innerRadius,outerRadius,20,20)
      glPopMatrix()




class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
            return self.data

    def getNext(self):
            return self.next

    def setData(self,newdata):
            self.data = newdata

    def setNext(self,newnext):
            self.next = newnext




