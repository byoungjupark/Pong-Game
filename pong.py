#Simple Pong in Python 3 for Beginners

import turtle #그래픽에 사용되는 모듈, pygame 모듈이 더 많이 사용되지만 beginner에겐 turtle이 적합
import os

wn = turtle.Screen() #바탕화면 생성
wn.title("Pong by @judy")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0) #turtle의 기본 모양은 화살표이고, 움직임의 흔적을 남긴다. 자취를 남기지 않기 위해 tracer메소드에 0의 값을 준다.

#Score
score_a = 0
score_b = 0

#Paddle A
paddle_a = turtle.Turtle() #객체 생성
paddle_a.speed(0) #움직이는 속도 (=그림을 그리는 속도)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1) #1 = 20px 이므로 width = 100px, length = 20px
paddle_a.penup() #펜을 올리는 명령어로 이 상태로 이동할 때에는 선을 그리지 않는다
paddle_a.goto(-350, 0) #처음 위치 설정

#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2 #d = delta, move by 2px everytime
ball.dy = -2 #x,y좌표 이동 방향(+-)과 간격(숫자)을 의미

#Pen 점수판
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle() #turtle을 화면에서 숨긴다
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

#Function 패들 이동 기능을 지닌 함수
def paddle_a_up():
    y = paddle_a.ycor() #ycor y축 / xcor x축
    y += 20
    paddle_a.sety(y) #sety: y좌표를 괄호 안의 숫자만큼 이동시킨다

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

#Keyboard binding
wn.listen() #screen 클래스는 listen 함수 제공함. 실행할 키를 반응시켜준다
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")


#Main game loop 
while True:
    wn.update() #화면의 변화를 업데이트 해준다

    #Move the ball 
    #while이 true일 동안 ball은 계속 +2가 된다
    ball.setx(ball.xcor() + ball.dx) #원래 x좌표에서 2px(dx값)만큼 이동시킨다
    ball.sety(ball.ycor() + ball.dy) #원래 y좌표에서 -2px(dy값)만큼 이동시킨다

    #Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1 #원래 방향의 반대로 이동한다
        os.system("afplay bounce.wav")

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system("afplay bounce.wav")
    
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
    
    #Paddle and ball collisions
    #패들의 길이는 100px. 공이 패들 y값(세로)안에 들어가게 될 범위는 -40~40이다. 
    #공이 이 범위 안에 든다는 것은 공이 패들에 맞았다는 의미
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor()+40 and ball.ycor() > paddle_b.ycor()-40):
        ball.setx(340)
        ball.dx *= -1
        os.system("afplay bounce.wav")

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor()+40 and ball.ycor() > paddle_a.ycor()-40):
        ball.setx(-340)
        ball.dx *= -1
        os.system("afplay bounce.wav")
