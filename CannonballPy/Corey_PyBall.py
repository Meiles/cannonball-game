import math
import pygame

class ball(object):

    Black = ( 0, 0 ,0)
    RED = (255, 0 ,0)

    def __init__(self, x, y, launchAngle, launchVelocity, timeInterval):
        self.x = x
        self.y = y
        self.xVelocity = launchVelocity * math.cos(launchAngle)
        self.yVelocity = launchVelocity * math.sin(launchAngle)
        selt.timeInterval = timeInterval
        self.xDelta = self.timeInterval * self.xVelocity
        self.ground = 650
        self.isMoving = True


    def move(self):
        self.prev_yVelocity = self.yVelocity
        self.yVelocity = self.yVelocity - (9.8 *self.timeInterval)
        self.y = (self.y + (self.timeInterval * (( prev_yVelocity + self.yVelocity / 2)))
        #self.y = max(self.y, 0)
        self.x += (self.xDelta)
        self.isMoving = (self.y > 0)

    def drawBall(self, window):
        ballPosition = (round(self.x), round(self.ground - self.y))
        pygame.draw.circle(window, ball.BLACK, ballPosition, 4)



