#!/usr/bin/env python

def main():
    import turtle

    class Paddle():
        def __init__(self, position):
            self.position = position
        def spawn(self):
            self.paddle = turtle.Turtle()
            self.paddle.shape('square')
            self.paddle.speed(0)
            self.paddle.goto(self.position, 0) 
            self.paddle.color('white')
            self.paddle.penup()
            self.paddle.shapesize(stretch_len=1, stretch_wid=5)
        def up(self):
            move = self.paddle.ycor()
            if move < 250:
                move += 20
                self.paddle.sety(move)
        def down(self):
            move = self.paddle.ycor()
            if move >= -250:
                move -= 20
                self.paddle.sety(move)

    class Ball():
        def spawn(self):
            self.ball = turtle.Turtle()
            self.ball.shape('square')
            self.ball.speed(0)
            self.ball.color('red')
            self.ball.penup()
        def reset(self):
            self.ball.goto(0, 0)
        def mx(self, ballDelta):
            xcoor = self.ball.xcor()
            move = xcoor + ballDelta
            self.ball.setx(move)
        def my(self, ballDelta):
            ycoor = self.ball.ycor()
            move = ycoor + ballDelta
            self.ball.sety(move)
        def getx(self):
            return self.ball.xcor()
        def gety(self):
            return self.ball.ycor()

    #Start window
    window = turtle.Screen()
    window.setup(width=800, height=600)
    window.bgcolor('black')

    #Spawn paddle
    paddle_left = Paddle(-350)
    paddle_left.spawn()

    paddle_right = Paddle(350)
    paddle_right.spawn()

    #Spawn ball
    deltaX= 4
    deltaY = 4
    ball = Ball()
    ball.spawn()


    #Get key
    window.listen()
    #Left paddle
    window.onkeypress(paddle_left.up, 'w')
    window.onkeypress(paddle_left.down, 's')
    #Right paddle
    window.onkeypress(paddle_right.up, 'Up')
    window.onkeypress(paddle_right.down, 'Down')

    #Window loop
    while True:
        #Update window
        window.update()
        
        #Ball physics
        print(ball.gety(), ball.gety())
        #Top border
        if ball.gety() > 290:
            deltaY *= -1
        #Bottom border
        if ball.gety() < -290:
            deltaY *= -1
        #Left border
        if ball.getx() < -390:
            deltaX *= -1
            ball.reset()
        #Right border
        if ball.getx() > 390:
            deltaX *= -1
            ball.reset()

        ball.mx(deltaX)
        ball.my(deltaY)

if __name__ == '__main__':
    main()
