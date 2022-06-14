import turtle 

glavni_prozor = turtle.Screen() 
glavni_prozor.title("Ping pong by DavidV")
glavni_prozor.bgcolor("black")
glavni_prozor.setup(width=800, height=600)
glavni_prozor.tracer(0)

# bodovi
score_crveni = 0 
score_plavi = 0 


# lijevi igrac
crveni = turtle.Turtle()
crveni.speed(0) 
crveni.shape("square") 
crveni.color("red") 
crveni.shapesize(stretch_wid=5, stretch_len=1) 
crveni.penup() 
crveni.goto(-350, 0) 

# desni igrac
plavi = turtle.Turtle()
plavi.speed(0) 
plavi.shape("square") 
plavi.color("blue") 
plavi.shapesize(stretch_wid=5, stretch_len=1) 
plavi.penup() 
plavi.goto(350, 0) 


# loptica
loptica = turtle.Turtle()
loptica.speed(0) 
loptica.shape("square") 
loptica.color("white") 
loptica.penup() 
loptica.goto(0, 0) 
loptica.dx = 0.5
loptica.dy = -0.5

# rezultat
pen = turtle.Turtle() 
pen.speed(0)  
pen.color("white") 
pen.penup() 
pen.hideturtle() 
pen.goto(0,260) 
pen.write("Crveni -> 0\t0 <- Plavi", align="center", font=("Courier", 24, "normal")) 

# funkcije
def crveni_up(): 
    y = crveni.ycor() 
    y += 20 
    crveni.sety(y) 

def crveni_down(): 
    y = crveni.ycor()
    y -= 20 
    crveni.sety(y) 

def plavi_up(): 
    y = plavi.ycor() 
    y += 20 
    plavi.sety(y) 

def plavi_down(): 
    y = plavi.ycor() 
    y -= 20 
    plavi.sety(y) 

# tipkovnica
glavni_prozor.listen() 
glavni_prozor.onkeypress(crveni_up, "w") 
glavni_prozor.onkeypress(crveni_down, "s") 
glavni_prozor.onkeypress(plavi_up, "Up") 
glavni_prozor.onkeypress(plavi_down, "Down") 

# Glavni dio igrice
while True:
    glavni_prozor.update()
    
    
    loptica.setx(loptica.xcor() + loptica.dx) 
    loptica.sety(loptica.ycor() + loptica.dy) 

    
    if loptica.ycor() > 290: 
        loptica.sety(290) 
        loptica.dy *= -1 
    
    if loptica.ycor() < -290: 
        loptica.sety(-290) 
        loptica.dy *= -1 

    if loptica.xcor() > 390: 
        loptica.goto(0, 0) 
        loptica.dx *= -1 
        score_crveni += 1 
        pen.clear() 
        pen.write("Crveni -> {}\t{} <- Plavi".format(score_crveni, score_plavi), align="center", font=("Courier", 24, "normal")) 

    if loptica.xcor() < -390: 
        loptica.goto(0, 0) 
        loptica.dx *= -1 
        pen.clear() 
        score_plavi += 1 
        pen.write("Crveni -> {}\t{} <- Plavi".format(score_crveni, score_plavi), align="center", font=("Courier", 24, "normal")) 

     
    if (loptica.xcor() > 340 and loptica.xcor() < 350) and (loptica.ycor() < plavi.ycor() + 50 and loptica.ycor() > plavi.ycor() - 50):   
        loptica.setx(340) 
        loptica.dx *= -1 

    
    if (loptica.xcor() < -340 and loptica.xcor() > -350) and (loptica.ycor() < crveni.ycor() + 50 and loptica.ycor() > crveni.ycor() - 50):
        loptica.setx(-340) 
        loptica.dx *= -1 
