from graphics import *
import random
import math

# Do not change these following 4 variables
margin = 10 # height of the paddle from the ground
moveIncrement = 15 # paddle movement
ballRadius = 15
BOUNCE_WAIT= 1200 

BALL_COUNT = 1  # If we change this, the number of ball changes!

class Timer:
    def __init__(self):
        self.value = 0


class Paddle:

    def __init__(self, color, width, height, coordx, win):
        self.color = color
        self.width = width
        self.height = height
        self.x = coordx
        self.shape = Rectangle(Point(self.x - int(self.width / 2), win.getHeight() - margin - self.height),
                               Point(self.x + int(self.width / 2), win.getHeight() - margin))
        self.shape.setFill(self.color)
        self.window = win
        self.shape.draw(self.window)

    def move_left(self):   # move paddle to the left by the amount of global variable moveIncrement
    
        
        self.x -= moveIncrement
        self.shape.move(-moveIncrement, 0)

    def move_right(self):  # move paddle to the right by the amount of global variable moveIncrement
    

        self.x += moveIncrement
        self.shape.move(moveIncrement, 0)







class Ball:

    def __init__(self, coordx, coordy, color, radius, x_direction, speed, win):
        self.shape = Circle(Point(coordx, coordy), radius)
        self.x = coordx
        self.y = coordy
        self.xMovement = 0 # Current x movement
        self.yMovement = 0 # Current y movement
        self.color = color
        self.window = win
        self.shape.setFill(self.color)
        self.shape.draw(self.window)
        self.radius = radius
        self.timer = 0
        self.x_direction = x_direction   # Initial x direction. This variable will be 0 or 1. 1:right 0:left
        self.speed = speed

    def is_moving(self):   
        
        return False

    def bounce(self, gameTimer, minX, maxX, maxY):
        # Calculating x-axis ball movement and bouncing
        # minX: min x coord. of paddle
        # maxX: max x coord. of paddle
        # maxY: max y coord. at which the ball can be move. If it goes further, it falls to the ground.

        global BOUNCE_WAIT
        gameOver = False

        if gameTimer >= self.timer + BOUNCE_WAIT:
            self.timer = gameTimer
            
            
            
            
            
            if self.xMovement == 1:
                self.x += self.speed
            elif self.xMovement == -1:
                self.x -= self.speed
            self.shape.move(self.xMovement * self.speed, self.yMovement * self.speed)
            
            
            return gameOver



def main():
    win = GraphWin("StudentId Pong Game", 300, 600) # Replace your student id
    lives = 2
    win.setBackground("Black")
    myPaddle = Paddle("White", 100, 15, 150, win)
    
    ColorsList = ["Cyan","Red","Green","Yellow"]   
    BallList = list()
    for i in range(BALL_COUNT):
        rand_speed = random.randint(5, 20) # random speed for ball
        # Note that the speed of the balls may vary depending on the hardware. If it is too fast or too slow, you can change the speed range for yourself while testing.
        # However, if you change these range, do not forget to reset these values to the initial limits before sending us.
        
        rand_direction = random.randint(0, 1) # This variable will be 0 or 1 randomly.
        ball = Ball(myPaddle.x - int(myPaddle.width/2) + i*30, win.getHeight() - margin - myPaddle.height - ballRadius, ColorsList[i%4] , ballRadius,rand_direction,rand_speed, win)
        BallList.append(ball)
    


    
    livesCounter = Text(Point(win.getWidth() - int(win.getWidth() / 5), 250), f'Lives -- {lives}')
    livesCounter.setTextColor("Cyan")
    livesCounter.setSize(15)
    livesCounter.draw(win)
    gameTimer = Timer()
    
    gameOver = False

    while lives > 0:
        while not gameOver:
            keyPress = win.checkKey()
            if keyPress == 'a': 
                myPaddle.move_left()
                
            if keyPress == 'd':
                myPaddle.move_right()
                
            if keyPress == 'l': # balls will move faster
                for item in BallList:
                    item.speed += 1  
                    
            if keyPress == 'k':  # Balls will move slower. Note that in our case min speed is 2.
                for item in BallList:
                    if item.speed > 2:
                        item.speed -= 1

            if keyPress == 's':  # Initial movement of balls
                for item in BallList:
                    if(not item.is_moving()):
                        if item.x_direction == 1:   # it means ball moves to right in x direction
                            item.xMovement = 1   
                        else:                   # it means ball moves to left in x direction
                            item.xMovement = -1
                        item.yMovement = -1 # at initial ball moves up in y direction


            gameTimer.value += 1
            for item in BallList:
                gameOver = item.bounce(gameTimer.value, (myPaddle.x-int(myPaddle.width/2)), (myPaddle.x+int(myPaddle.width/2)), win.getHeight() - margin - myPaddle.height)
                if gameOver == True:
                    break

main()




