from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from VectorPy import *
import sys



def myRand():
    return double(double(rand()) / RAND_MAX)

collisionDamping = 0.3
damping = 0.95


class Ball:
    center = Vector3d(0,0,0)
    velocity = Vector3d(0,0,0)
    oldVelocity = Vector3d(0,0,0)
    accel = Vector3d(0,0,0)
    color = Vector3d(0,0,0)
    vel = Vector3d(0,0,0)
    radius = 0.0
    bbx = 0.0 

    def __init__(self, radius, center, vel, accel, bbx):
        self._radius = radius
        self._center = center
        self._vel = velocity
        self._accel = accel
        self._bbx = bbx


    def Ball(self):
        center.SetAll(0,0,0)
        velocity.SetAll(0,0,0)
        accel.SetAll(0,0,0)
        color.SetAll(0.3,0.2,0.8)


    #def SetRandomColor(self):


    def IsMoving(self):
        if(velocity.normalize() < 0.2):
            return True
        else:
            return False


    def Update(self, dt):
        center = center + velocity * dt
        oldvelocity = velocity
        velocity = velocity + accel * dt
        oldAccelY = accel.GetY()
        oldAccelY -= 9.8
        accel.SetY(oldAccelY)
        accel *= damping

        RevovleCollision()

        if(accel.normalize() < 0.5):
            accel.SetAll(0,0,0)

        if(velocity.normalize() < 0.5):
            velocity.SetAll(0,0,0)



    def RevovleCollision(self):

        if(center.GetX() - radius < bbx[0]):
            oldCenterX = center.GetX()

            center.SetX(bbx[0] + radius)

            velocity.SetX(-1 * velocity.GetX())
            velocity *= collisionDamping
            accel *= collisionDamping

        if(center.GetX() - radius < bbx[1]):
            oldCenterX = center.GetX()

            center.SetX(bbx[1] - radius)

            velocity.SetX(-1 * velocity.GetX())
            velocity *= collisionDamping
            accel *= collisionDamping

        if(center.GetY() - radius < bbx[2]):
            oldCenterY = center.GetY()

            center.SetY(bbx[0] + radius)

            velocity.SetY(-1 * velocity.GetY())
            velocity *= collisionDamping
            accel *= collisionDamping

        if(center.GetY() - radius < bbx[3]):
            oldCenterY = center.GetY()

            center.SetY(bbx[3] - radius)

            velocity.SetY(-1 * velocity.GetY())
            velocity *= collisionDamping
            accel *= collisionDamping

        if(center.GetZ() - radius < bbx[4]):
            oldCenterZ = center.GetZ()

            center.SetZ(bbx[4] + radius)

            velocity.SetZ(-1 * velocity.GetZ())
            velocity *= collisionDamping
            accel *= collisionDamping


        if(center.GetZ() - radius < bbx[5]):
            oldCenterZ = center.GetZ()

            center.SetZ(bbx[5] - radius)

            velocity.SetZ(-1 * velocity.GetZ())
            velocity *= collisionDamping
            accel *= collisionDamping




    def Draw(self):
        glColor3f(color.GetX(), color.GetY(), color.GetZ())
        glPushMatrix()
        glTranslated(center[0], center[1], center[2])
        glutSolidSphere(radius,10,10)
        glPopMatrix()
        glPointSize(3)
        glColor3f(1,0,0)
        glBegin(GL_POINTS)
        glVertex3d(center[0],center[1],center[2])
        glEnd()
        glFlush()