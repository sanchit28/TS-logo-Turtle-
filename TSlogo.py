import turtle
skk = turtle.Turtle() 

my_window = turtle.Screen() 
my_window.bgcolor("grey")
T_color = "red"
S_color = "dark blue"
skk.fillcolor(T_color) 
#red fill starts
skk.begin_fill()
skk.pensize(1)

#up1 step1
skk.left(90)
skk.forward(175)
#left1 step 2
skk.left(90)
skk.forward(130)
#down1 step 3
skk.left(90)
skk.forward(35)
#right1 step 4
skk.left(90)
skk.forward(95)
#down2 step 5
skk.right(90)
skk.forward(140)
#left2 step 6
skk.left(90)
skk.forward(130)
#red fill end
skk.end_fill()

#'S' starts
skk.fillcolor(S_color)
#Blue fill start
skk.begin_fill()

#up1 step1
skk.left(90)
skk.forward(100)
#left1 step2
skk.left(90)
skk.forward(55)
#right1 step3
skk.right(90)
skk.forward(35)
#right2 step 4
skk.right(90)
skk.forward(95)
#up2 step5
skk.left(90)
skk.forward(38)     # chk after
#left2 step6
skk.left(90)
skk.forward(130)
#down1 step 7
skk.left(90)
skk.forward(100)
#right step 8
skk.left(90)
skk.forward(55)
#right step 9
skk.right(90)
skk.forward(35)
#left step 10
skk.right(90)
skk.forward(55)
#step11
skk.left(90)
skk.forward(38)
skk.end_fill()

skk.up()
turtle.done()