import faulthandler; faulthandler.enable()
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from BallPy import *
from TargetPy import *
from VectorPy import *
import sys
window = 0
red = 255.0
blue = 255.0
green = 255.0

dt = 0.02
yPlane = -4

head = Node

ball = Ball

target = Target

cannon = Vector3d(0,0,0)

curRadius = 0.6
minRadius = 0.6
maxRadius = 0.6

maxAccel = 850

cannonL = 0.5
minCannonL = 0.25
maxCannonL = 1.5

angle1 = 45.0
angle2 = 165.0

bbx = [-20,20,-4,20,-100,100]

def init(self): 
   mat_specular = GLfloat[ 1.0, 1.0, 1.0, 0.0 ]
   mat_shininess = GLfloat[10.0]
   light_position = GLfloat[1.0, 1.0, 1.0, 0.0]
   light_ambient = GLfloat[0.8, 0.8, 0.8, 1.0 ]
   light_diffuse = GLfloat[1.0, 1.0, 1.0, 1.0 ]
   light_specular = GLfloat[0.8, 0.8, 0.8, 1.0]
   glClearColor (0.0, 0.0, 0.0, 0.0)
   glShadeModel (GL_SMOOTH)

   glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, mat_specular);
   glMaterialfv(GL_FRONT_AND_BACK, GL_SHININESS, mat_shininess);


   glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient);
   glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse);
   glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular);
   glLightfv(GL_LIGHT0, GL_POSITION, light_position);

   glEnable(GL_LIGHTING);
   glEnable(GL_LIGHT0);
   glEnable(GL_DEPTH_TEST);


w = 100
h = 100

def changeSize(self, w, h):

    #Prevent a divide by zero, when window is too short
    #(you cant make a window of zero width).
    if (h == 0):
        h = 1
        ratio =  w * 1.0 / h

        #Use the Projection Matrix
    glMatrixMode(GL_PROJECTION);

        #Reset Matrix
    glLoadIdentity();

    #Set the viewport to be the entire window
    glViewport(0, 0, w, h);

    #Set the correct perspective.
    gluPerspective(45.0, ratio, 0.1, 1000.0);

    #Get Back to the Modelview
    glMatrixMode(GL_MODELVIEW);

'''
glEnable(GL_LIGHTING);
glEnable(GL_LIGHT0);
GLfloat lightpos[] = {.5, 1., 1., 0.};
glLightfv(GL_LIGHT0, GL_POSITION, lightpos);
'''

def drawBBX(self):
  glShadeModel (GL_SMOOTH)
  glNormal3d(1,0,0)
  glColor3f(1,0,0)
  glBegin(GL_QUADS) #left side
  glVertex3d(bbx[0],bbx[2],bbx[4])
  glVertex3d(bbx[0],bbx[3],bbx[4])
  glVertex3d(bbx[0],bbx[3],bbx[5])
  glVertex3d(bbx[0],bbx[2],bbx[5])
  glEnd()

  glNormal3d(-1,0,0)
  glColor3f(0,0,1)
  glBegin(GL_QUADS); #right side
  glVertex3d(bbx[1],bbx[2],bbx[4])
  glVertex3d(bbx[1],bbx[3],bbx[4])
  glVertex3d(bbx[1],bbx[3],bbx[5])
  glVertex3d(bbx[1],bbx[2],bbx[5])
  glEnd()

  glNormal3d(0,1,0)
  glColor3f(0.8,0.8,0.8)
  glBegin(GL_QUADS) #bottom side
  glVertex3d(bbx[0],bbx[2],bbx[4])
  glVertex3d(bbx[0],bbx[2],bbx[5])
  glVertex3d(bbx[1],bbx[2],bbx[5])
  glVertex3d(bbx[1],bbx[2],bbx[4])
  glEnd()

  glNormal3d(0,-1,0)
  glColor3f(0.0,0.8,0.2)
  glBegin(GL_QUADS) #top side
  glVertex3d(bbx[0],bbx[3],bbx[4])
  glVertex3d(bbx[0],bbx[3],bbx[5])
  glVertex3d(bbx[1],bbx[3],bbx[5])
  glVertex3d(bbx[1],bbx[3],bbx[4])
  glEnd()

  #back
  glNormal3d(0,0,-1)
  glColor3f(0.0,0.8,0.8)
  glBegin(GL_QUADS) #back side
  glVertex3d(bbx[0],bbx[2],bbx[4])
  glVertex3d(bbx[0],bbx[3],bbx[4])
  glVertex3d(bbx[1],bbx[3],bbx[4])
  glVertex3d(bbx[1],bbx[2],bbx[4])
  glEnd()
  #front
  glNormal3d(0,0,1)
  glColor3f(0.0,0.8,0.8)
  glBegin(GL_QUADS) #front side
  glVertex3d(bbx[0],bbx[2],bbx[5])
  glVertex3d(bbx[0],bbx[3],bbx[5])
  glVertex3d(bbx[1],bbx[3],bbx[5])
  glVertex3d(bbx[1],bbx[2],bbx[5])
  glEnd()


def getCannonEndPts(self, angle1, angle2, cX, cY):
    cX = cannon.GetX()+cannonL * cosd(angle1)
    cY = cannon.GetY()+cannonL * sind(angle1)


def getCannonEndPts(self, angle1, angle2, cX, cY, cZ):
    cX = cannon.GetX()+cannonL * sind(angle1)
    cY = cannon.GetY()+cannonL * sind(angle2)
    cz = cannon.GetZ()+cannonL * cosd(angle2)

def DrawAllBalls(self):
    tmp = head
    while(tmp != None):
        tmp = BallPy.ball.Draw()
        tmp = TargetPy.Node.getNext()

def UpdateAllBalls(self):
    tmp = head
    while(tmp != None):
        tmp = BallPy.ball.Draw()
        tmp = TargetPy.Node.getNext()


r = 0.0
stPt = Vector3d(0,0,0)
vel = Vector3d(0,0,0)
accelVec = Vector3d(0,0,0)

'''
def AddBall(sef):
    newBall = TargetPy.Node()
    newBall = Ball.SetValues(curRadius, stPt, vel, accelVec)
    newBall = ball.SetRandomColor()
    newBall = newBall.getNext()
    newBall = head
    head = newBall
'''


#def RemoveAllNonMoving(self):


def renderScene(self):
    glEnable(GL_DEPTH_TEST) 

    #Clear Color and Depth Buffers
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(0.5, 0.5, 0.5, 1.0)          # background is gray

    #Reset transformations
    glLoadIdentity();

    #Set the camera
    gluLookAt(0.0, 0.0, 10.0,
        0.0, 0.0,  0.0,
        0.0, 255.0,  0.0)

    #Enable lighting
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)

    #draw bbx
    drawBBX()

    #draw yPlane
    glLineWidth(2);
    glBegin(GL_LINES);  #draw the yPlane
    glVertex3f(-4.0,yPlane, 0.0)
    glVertex3f(4.0,yPlane, 0.0)
    glEnd()

    #draw the ball(s)
    #ball.Draw();
    DrawAllBalls()
    target.Draw()

    #draw the cannon
    #double cX #<<next 3 lines, for 2d
    #double cY
    #getCannonEndPts(angle1,cX,cY)
    #double cX
    #double cY
    #double cZ
    getCannonEndPts3D(angle1, angle2 ,cX,cY,cZ)
    glColor3f(0,0,1)
    glLineWidth(2)
    glBegin(GL_LINES)  #draw the yPlane
    glVertex3f(cannon.GetX(), cannon.GetY(), cannon.GetZ())
    glVertex3f(cX, cY, cZ)
    glEnd()

    #ball.Update(dt)
    UpdateAllBalls()
    target.Update(head) 

    glutSwapBuffers()

key = 0
x = 0
y = 0

def processNormalKeys(self, key, x, y):
    if(key == 27 or key == 'q'): #quit
        sys.exit()
    elif(key=='s'): #shoot
        cX, cY, cZ = 0.0, 0.0, 0.0
        getCannonEndPts(angle1, angle2, cX, cY, cZ)
        accel = maxAccel * (cannonL/maxCannonL)
        stPt = Vector3d(cX, cY+curRadius, cZ)
        vel = Vector3d(0,0,0)
        accelVec = Vector3d(cX-cannon.GetX(), cY-cannon.GetY(), cZ-cannon.GetZ())
        accelVec.selfNormalize()
        accelVec.selfScale()
        AddBall(curRadius,stPt,vel,accelVec)
    elif(key=='d'):
        RemoveAllNonMoving()
    elif(key=='1'):
        cannonL -= 0.02
        if(cannonL<minCannonL):
            cannonL = minCannonL
    elif(key=='2'):
        cannonL += 0.02
        if(cannonL>maxCannonL):
            cannonL = maxCannonL
    elif(key=='9'):
        curRadius -= 0.2
        if(curRadius<minRadius):
            curRadius = minRadius
    elif(key=='0'):
        curRadius += 0.2
        if(curRadius>maxRadius):
            curRadius = maxRadius

def processSpecialKeys(self, key, x, y):
    if(key==GLUT_KEY_UP):
        angle1+=1
        if(angle1>=100):
            angle1 = 100
            #break

    if(key==GLUT_KEY_DOWN):
        angle1 -= 1
        if(angle1<=0):
            angle1 = 0
            #break

    if(key==GLUT_KEY_LEFT):
        angle2 += 1
        if(angle2>=270):
            angle2 = 270
            #break

    if(key==GLUT_KEY_RIGHT):
        angle2 -= 1
        if(angle2<=90):
            angle2 = 90




'''
#tries to trace faults
def trace(frame, event, arg):
    print("%s, %s:%d" % (event, frame.f_code.co_filename, frame.f_lineno))
    return trace

def test():
    print ("Line: ")

sys.settrace(trace)
test()
'''


argc = 1
argsv = ''
def main(self, argc, argsv):
    #cannon.SetAll(-4,yPlane,0);
    cannon.SetAll(0,yPlane,0)
    #set the target bbx
    target.SetBBX(bbx)
    return 1

#init GLUT and create window
    glutInit(argc,argsv)
    glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGBA)
    glLoadIdentity()
    glutSwapBuffers()       
    glutInitWindowPosition(100,100)
    glutInitWindowSize(320,320)
    window = glutCreateWindow("ShootPts")

    init()
    #register callbacks
    glutDisplayFunc(main)
    glutReshapeFunc(main)
    glutIdleFunc(main)

    #here are the new entries
    glutKeyboardFunc(processNormalKeys)
    glutSpecialFunc(processSpecialKeys)

    #enter GLUT event processing cycle
    glutMainLoop()
    renderScene()
    main()

#if __name__ == '__main__':
 # main()


