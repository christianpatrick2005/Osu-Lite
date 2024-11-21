import turtle
import pygame

def credit():
    pygame.mixer.init()
    pygame.mixer.music.load("Different Heaven - Safe And Sound _ House _ NCS - Copyright Free Music.mp3")
    pygame.mixer.music.play(-1)#beri -1 agar lagu tetap berjalan meski ganti ganti menu
    #membuat screen
    ac = turtle.Screen()
    ac.title("credit 1")
    ac.bgcolor("black")
    ac.setup(width=800,height=600)#untuk ukuran
    ac.tracer(0)  

    # wadah tempat tulisan
    ball2 = turtle.Turtle()
    ball2.shape("circle")
    ball2.color("white")
    ball2.turtlesize(2)#ukuran bola
    ball2.penup()#menghilangkan garis
    ball2.goto(-240,260)#kordinat animasi
    ball2.hideturtle()
    ball2.write(f"produced by :", align="center", font=("inline", 12, "normal"))

    pilih1 = turtle.Turtle()
    pilih1.shape("square")
    pilih1.color("white")
    pilih1.shapesize(3,14)#panjang,lebar,tebal
    pilih1.penup()#menghilangkan garis
    pilih1.goto(0,260)
    pilih1.hideturtle()
    pilih1.write(f"published by :", align="center", font=("inline", 12, "normal"))

    pilih2 = turtle.Turtle()
    pilih2.shape("square")
    pilih2.color("white")
    pilih2.shapesize(3,14)#panjang,lebar,tebal
    pilih2.penup()#menghilangkan garis
    pilih2.goto(240,260)
    pilih2.hideturtle()
    pilih2.write(f"designed by :", align="center", font=("inline", 12, "normal"))

    pilih3 = turtle.Turtle()
    pilih3.shape("square")
    pilih3.color("white")
    pilih3.shapesize(3,14)#panjang,lebar,tebal
    pilih3.penup()#menghilangkan garis
    pilih3.goto(-240,230)
    pilih3.hideturtle()
    pilih3.write(f"Christian Patrick", align="center", font=("inline", 12, "normal"))

    pilih4 = turtle.Turtle()
    pilih4.shape("square")
    pilih4.color("white")
    pilih4.shapesize(3,14)#panjang,lebar,tebal
    pilih4.penup()#menghilangkan garis
    pilih4.goto(0,230)
    pilih4.hideturtle()
    pilih4.write(f"Christian Patrick", align="center", font=("inline", 12, "normal"))

    pilih5 = turtle.Turtle()
    pilih5.shape("square")
    pilih5.color("white")
    pilih5.shapesize(3,14)#panjang,lebar,tebal
    pilih5.penup()#menghilangkan garis
    pilih5.goto(240,230)
    pilih5.hideturtle()
    pilih5.write(f"Christian Patrick", align="center", font=("inline", 12, "normal"))

    pilih6 = turtle.Turtle()
    pilih6.shape("square")
    pilih6.color("white")
    pilih6.shapesize(3,14)#panjang,lebar,tebal
    pilih6.penup()#menghilangkan garis
    pilih6.goto(0,90)
    pilih6.hideturtle()
    pilih6.write(f"Thanks to :", align="center", font=("inline", 12, "normal"))

    pilih7 = turtle.Turtle()
    pilih7.shape("square")
    pilih7.color("white")
    pilih7.shapesize(3,14)#panjang,lebar,tebal
    pilih7.penup()#menghilangkan garis
    pilih7.goto(0,170)
    pilih7.hideturtle()
    pilih7.write(f"Sound by :", align="center", font=("inline", 12, "normal"))

    pilih8 = turtle.Turtle()
    pilih8.shape("square")
    pilih8.color("white")
    pilih8.shapesize(3,14)#panjang,lebar,tebal
    pilih8.penup()#menghilangkan garis
    pilih8.goto(0,140)
    pilih8.hideturtle()
    pilih8.write(f"Alan Walker, RADWIMPS, TK, King Gnu, Eve", align="center", font=("inline", 12, "normal"))

    pilih9 = turtle.Turtle()
    pilih9.shape("square")
    pilih9.color("white")
    pilih9.shapesize(3,14)#panjang,lebar,tebal
    pilih9.penup()#menghilangkan garis
    pilih9.goto(0,60)
    pilih9.hideturtle()
    pilih9.write(f"Pak Edwin Meinardi Trianto dan seluruh mahasiswa FTI angkatan 2023", align="center", font=("inline", 12, "normal"))

    pilih10 = turtle.Turtle()
    pilih10.shape("square")
    pilih10.color("white")
    pilih10.shapesize(3,14)#panjang,lebar,tebal
    pilih10.penup()#menghilangkan garis
    pilih10.goto(0,10)
    pilih10.hideturtle()
    pilih10.write(f"Supported by :", align="center", font=("inline", 12, "normal"))

    ac.addshape("ezgif.com-resize (1).gif")
    ac.addshape("ezgif.com-resize (2).gif")
    ac.addshape("ezgif.com-resize (3).gif")

    pilih11 = turtle.Turtle()
    pilih11.shape("ezgif.com-resize (1).gif")
    pilih11.color("white")
    pilih11.penup()  # menghilangkan garis
    pilih11.goto(170, -50)
    pilih11.showturtle()

    pilih11 = turtle.Turtle()
    pilih11.shape("ezgif.com-resize (2).gif")
    pilih11.color("white")
    pilih11.penup()  # menghilangkan garis
    pilih11.goto(-100, -50)
    pilih11.showturtle()

    pilih11 = turtle.Turtle()
    pilih11.shape("ezgif.com-resize (3).gif")
    pilih11.color("white")
    pilih11.penup()  # menghilangkan garis
    pilih11.goto(0, -200)
    pilih11.showturtle()

    def switch_credit(x,y):
        # Hentikan screen sebelumnya dan pindah ke credit2
        ac.clearscreen()
        # turtle.bye()
        credit2()

    while True:
        ac.update()
        ac.onclick(switch_credit)


def credit2():
    #membuat screen
    ab = turtle.Screen()
    ab.title("credit 2")
    ab.bgcolor("black")
    ab.setup(width=800,height=600)#untuk ukuran
    ab.tracer(0)  

    # wadah tempat tulisan

    pilih1 = turtle.Turtle()
    pilih1.shape("square")
    pilih1.color("white")
    pilih1.shapesize(3,14)#panjang,lebar,tebal
    pilih1.penup()#menghilangkan garis
    pilih1.goto(0,260)
    pilih1.hideturtle()
    pilih1.write(f"Sponsored by :", align="center", font=("inline", 12, "normal"))

    pilih6 = turtle.Turtle()
    pilih6.shape("square")
    pilih6.color("white")
    pilih6.shapesize(3,14)#panjang,lebar,tebal
    pilih6.penup()#menghilangkan garis
    pilih6.goto(0,90)
    pilih6.hideturtle()
    pilih6.write(f"Special Thanks to :", align="center", font=("inline", 12, "normal"))

    ab.addshape("ezgif.com-resize (4).gif")
    ab.addshape("ezgif.com-resize (5).gif")
    ab.addshape("ezgif.com-resize (6).gif")
    ab.addshape("ezgif.com-resize (7).gif")

    pilih4 = turtle.Turtle()
    pilih4.shape("ezgif.com-resize (4).gif")
    pilih4.color("white")
    pilih4.penup()#menghilangkan garis
    pilih4.goto(0,200)

    pilih4 = turtle.Turtle()
    pilih4.shape("ezgif.com-resize (5).gif")
    pilih4.color("white")
    pilih4.penup()#menghilangkan garis
    pilih4.goto(-100,-10)

    pilih4 = turtle.Turtle()
    pilih4.shape("ezgif.com-resize (6).gif")
    pilih4.color("white")
    pilih4.penup()#menghilangkan garis
    pilih4.goto(80,-10)

    pilih4 = turtle.Turtle()
    pilih4.shape("ezgif.com-resize (7).gif")
    pilih4.color("white")
    pilih4.penup()#menghilangkan garis
    pilih4.goto(0,-180)

    def switch_credit2(x,y):
        # Hentikan screen sebelumnya dan pindah ke credit2
        ab.clearscreen()
        # turtle.bye()
        credit3()

    while True:
        ab.update()
        ab.onclick(switch_credit2)

def credit3():
    #membuat screen
    aa = turtle.Screen()
    aa.title("credit 3")
    aa.bgcolor("black")
    aa.setup(width=800,height=600)#untuk ukuran
    aa.tracer(0)

    pilih2 = turtle.Turtle()
    pilih2.shape("square")
    pilih2.color("white")
    pilih2.shapesize(3,14)#panjang,lebar,tebal
    pilih2.penup()#menghilangkan garis
    pilih2.goto(0,200)
    pilih2.hideturtle()
    pilih2.write(f"The End", align="center", font=("inline", 50, "normal"))

    pilih3 = turtle.Turtle()
    pilih3.shape("square")
    pilih3.color("white")
    pilih3.shapesize(3,14)#panjang,lebar,tebal
    pilih3.penup()#menghilangkan garis
    pilih3.goto(0,170)
    pilih3.hideturtle()
    pilih3.write(f"Press u to exit", align="center", font=("inline", 10, "normal"))

    aa.addshape("ezgif.com-resize (8).gif")

    pilih4 = turtle.Turtle()
    pilih4.shape("ezgif.com-resize (8).gif")
    pilih4.color("white")
    pilih4.penup()#menghilangkan garis
    pilih4.goto(0,-50)

    pilih1 = turtle.Turtle()
    pilih1.shape("square")
    pilih1.color("white")
    pilih1.shapesize(3,14)#panjang,lebar,tebal
    pilih1.penup()#menghilangkan garis
    pilih1.goto(0,-260)
    pilih1.hideturtle()
    pilih1.write(f"Copyright (c) 2023 - ppy powered 2007-2023", align="center", font=("inline", 10, "normal"))

    # def keluargame():
    #     aa.bye()

    aa.listen()

    while True:
        aa.update()
        # aa.onkeypress(keluargame,"u")
        aa.exitonclick()
        pygame.mixer.music.stop()
