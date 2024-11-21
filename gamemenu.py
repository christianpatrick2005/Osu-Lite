import turtle
import pygame
import time
import random

pygame.init()

gameoverlist = []

def kerangkagame():
    #membuat screen
    wn = turtle.Screen()
    wn.title("kerangka game")
    wn.bgcolor("black")
    wn.setup(width=800,height=600)#untuk ukuran
    wn.tracer(0)

    wn.addshape("ezgif.com-resize.gif")
    k = True

    listtriangle = []
    listbullet = []

    #memasukkan gambar score
    score = 0 #score dimulai dr nol
    titleScore = turtle.Turtle()
    titleScore.shape("ezgif.com-resize.gif")
    titleScore.color("white")
    titleScore.penup()
    titleScore.goto(0, 260)

    kel1 = turtle.Turtle()
    kel1.shape("square")
    kel1.color("white")
    kel1.shapesize(3,14)#panjang,lebar,tebal
    kel1.penup()#menghilangkan garis
    kel1.goto(-200,260)
    kel1.hideturtle()
    kel1.write(f"Press q to skip", align="center", font=("inline", 15, "normal"))

    #membuat = "score"
    angkascore = turtle.Turtle()
    angkascore.shape("square")
    angkascore.color("white")
    angkascore.penup()
    angkascore.hideturtle()
    angkascore.goto(130, 245)
    angkascore.write(f"= {score}", align="center", font=("inline", 24, "normal"))

    triangle = None #inisialisasi variable triangle sbg variable global

    # membuat segitiga random jatuh kebawah
    def spawntriangle(x , y):
        global triangle
        triangle = turtle.Turtle()
        triangle.shape("classic")
        triangle.color("white")
        triangle.turtlesize(4)
        triangle.left(90)
        triangle.penup()
        triangle.speed(random.randint(3,6))
        triangle.goto(x , y)#koordinat triangle berdasarkan x dan y
        listtriangle.append(triangle)

    #membuat panah
    arrow1 = turtle.Turtle()
    arrow1.shape("classic")
    arrow1.color("lightgreen")
    arrow1.turtlesize(4)
    arrow1.penup()#menghilangkan garis
    arrow1.goto(-200,-180)#kordinat animasi

    arrow2 = turtle.Turtle()
    arrow2.shape("classic")
    arrow2.color("pink")
    arrow2.turtlesize(4)
    arrow2.penup()#menghilangkan garis
    arrow2.goto(-100,-180)#kordinat animasi
    # arrow2.left(90)

    arrow3 = turtle.Turtle()
    arrow3.shape("classic")
    arrow3.color("lightblue")
    arrow3.turtlesize(4)
    arrow3.penup()#menghilangkan garis
    arrow3.goto(10,-180)#kordinat animasi
    # arrow3.left(180)

    arrow4 = turtle.Turtle()
    arrow4.shape("classic")
    arrow4.color("red")
    arrow4.turtlesize(4)
    arrow4.penup()#menghilangkan garis
    arrow4.goto(120,-180)#kordinat animasi
    # arrow4.right(90)

    def arrow1press():
        bullet = turtle.Turtle()
        bullet.shape("square")
        bullet.color("orange")
        bullet.shapesize(3,0.5)
        bullet.penup()
        bullet.left(90)
        bullet.dx = 100 #menggerakkan peluru ke kanan sebesar 20 pixel setiap loop
        bullet.goto(arrow1.xcor()+30,arrow1.ycor())#mengatur start peluru dimulai dari hasil penjumlahan dari kordinat x arrow dan 5
        listbullet.append(bullet)

    def arrow2press():
        bullet = turtle.Turtle()
        bullet.shape("square")
        bullet.color("orange")
        bullet.shapesize(3,0.5)
        bullet.penup()
        bullet.left(90)
        bullet.dx = 100 #menggerakkan peluru ke kanan sebesar 20 pixel setiap loop
        bullet.goto(arrow2.xcor()+30,arrow2.ycor())#mengatur start peluru dimulai dari hasil penjumlahan dari kordinat x arrow dan 5
        listbullet.append(bullet)

    def arrow3press():
        bullet = turtle.Turtle()
        bullet.shape("square")
        bullet.color("orange")
        bullet.shapesize(3,0.5)
        bullet.penup()
        bullet.left(90)
        bullet.dx = 100 #menggerakkan peluru ke kanan sebesar 20 pixel setiap loop
        bullet.goto(arrow3.xcor()+30,arrow3.ycor())#mengatur start peluru dimulai dari hasil penjumlahan dari kordinat x arrow dan 5
        listbullet.append(bullet)

    def arrow4press():
        bullet = turtle.Turtle()
        bullet.shape("square")
        bullet.color("orange")
        bullet.shapesize(3,0.5)
        bullet.penup()
        bullet.left(90)
        bullet.dx = 100 #menggerakkan peluru ke kanan sebesar 20 pixel setiap loop
        bullet.goto(arrow4.xcor()+30,arrow4.ycor())#mengatur start peluru dimulai dari hasil penjumlahan dari kordinat x arrow dan 5
        listbullet.append(bullet)

    def movebullets():
        for bullet in listbullet.copy():
            #mengecek apakah peluru keluar dr batasan yg ditentukan yaitu -200
            if bullet.xcor() > -200:
                bullet.hideturtle()  #menyembunyikan peluru / menghilangkan
                listbullet.remove(bullet)

    def tubrukan(bullets, triangle):
        return ((bullets.xcor() - triangle.xcor())**2 + (bullets.ycor() - triangle.ycor())**2)**0.5 #mengecek selisih dr koordinat antara triangle dan bullets yg ada apakah lbh kecil dr batas yg ditentukan

    def skip():
        pygame.mixer.music.stop()
        wn.clearscreen()
        gamemenu()

    wn.listen()
    wn.onkeypress(arrow1press,"a")
    wn.onkeypress(arrow2press,"s")
    wn.onkeypress(arrow3press,"d")
    wn.onkeypress(arrow4press,"f")
    wn.onkeypress(skip,"q")

    def gameovermenu():
        end = turtle.Screen()
        end.title("gameover")
        end.bgcolor("black")
        end.setup(width=800,height=600)

        end1 = turtle.Turtle()
        end1.shape("square")
        end1.color("white")
        end1.penup()
        end1.hideturtle()
        end1.goto(0, 245)
        end1.write(f" SCORE = {score}", align="center", font=("inline", 24, "normal"))

        end2 = turtle.Turtle()
        end2.shape("square")
        end2.color("red")
        end2.penup()
        end2.hideturtle()
        end2.goto(0, 0)
        end2.write(f"GAME OVER", align="center", font=("inline", 50, "normal"))

        # end3 = turtle.Turtle()
        # end3.shape("square")
        # end3.color("black")
        # end3.penup()
        # end3.hideturtle()
        # end3.goto(-150, -100)
        # end3.write(f"Press 'e' to retry", align="center", font=("inline", 24, "normal"))

        end4 = turtle.Turtle()
        end4.shape("square")
        end4.color("white")
        end4.penup()
        end4.hideturtle()
        end4.goto(0, -100)
        end4.write(f"Press 'u' to exit", align="center", font=("inline", 24, "normal"))

        def keluar():
            end.clearscreen()
            gamemenu()

        j = True 
        end.listen()

        while j == True:
            end.update()
            # turtle.textinput("space") #untuk merespon inputan text
            # turtle.onscreenclick(keluar) # untuk merespon inputan mouse
            end.onkey(keluar, 'u')
            # turtle.onkey(retry, 'e')


    triangle = None

    def keluarbatas():
        for triangle in listtriangle:
            #mengecek apakah triangle keluar dr batasan yg ditentukan yaitu -250
            if triangle.ycor() < -250:
                triangle.hideturtle() 
                 #menyembunyikan triangle / menghilangkan
                listtriangle.remove(triangle)

    while k == True :
        wn.update()
        time.sleep(0.2)
        # mengatur intensitas kemunculan triangle
        if random.randint(1,10) == 2 : # Fungsi ini kemungkinan berjalan adalah sekitar 1 dari 10 kali (kira-kira 10% peluang). Jika hasil dari random.randint(1,10) adalah 2, maka fungsi spawntriangle(-170, 280) akan dipanggil.
            spawntriangle(-170, 280)
        if random.randint(1,20) == 2:
            spawntriangle(-60, 280)
        if random.randint(1,30) == 2:
            spawntriangle(40, 280)
        if random.randint(1,15) == 10:
            spawntriangle(160, 280)

        
        # biar segitiganya bisa turun
        for i in listtriangle:
            i.sety(i.ycor() - 15)#triangle diset di koordinat y dan akan bergerak sebesar 15 pixel kebawah

        for bullet in listbullet:
            for triangle in listtriangle:
                if tubrukan(bullet, triangle) < 20: #menentukan hitbox triangle
                    triangle.hideturtle()
                    bullet.hideturtle()
                    listtriangle.remove(triangle)                   
                    # listbullet.remove(bullet)
                    #membuat score
                    titleScore.color("purple")
                    score += 1
                    angkascore.clear()
                    angkascore.write(f"= {score}", align="center", font=("inline", 24, "normal"))               

        # pergerakan bullet
        for i in listbullet:
            #set kordinat x awal dan koordinat x dr i ditambabah koordinat dx = 20)
            i.setx(i.xcor() + i.dx) # dx = menggerakkan peluru ke kanan sebesar dx pixel setiap loop
        
        movebullets()
        keluarbatas()

        #menentukan apakah musik msh diputar atau tdk
        if pygame.mixer.music.get_busy() == 0 : # untuk mengecek apakah musik berhenti dengan cara menanyakan apakah music == 0(false)
            pygame.mixer.music.stop()
            wn.clearscreen() #menghapus screen sebelumnya
            gameovermenu()
            # gamemenu()
            # turtle.bye()
            # k = False
        wn.update()

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

    def keluargame():
        pygame.mixer.music.stop()
        aa.clearscreen()
        gamemenu()

    aa.listen()

    while True:
        aa.update()
        aa.onkeypress(keluargame,"u")
        # aa.exitonclick()

def gamemenu():
        #membuat screen
        dc = turtle.Screen()
        dc.title("game menu")
        dc.bgcolor("black")
        dc.setup(width=800,height=600)#untuk ukuran
        dc.tracer(0)

        ball = turtle.Turtle()
        ball.shape("circle")
        ball.color("white")
        ball.turtlesize(15)#ukuran bola
        ball.penup()#menghilangkan garis
        ball.goto(-200,0)#kordinat animasi

        ball1 = turtle.Turtle()
        ball1.shape("circle")
        ball1.color("pink")
        ball1.turtlesize(13)#ukuran bola
        ball1.penup()#menghilangkan garis
        ball1.goto(-200,0)#kordinat animasi

        # wadah tempat tulisan
        ball2 = turtle.Turtle()
        ball2.shape("circle")
        ball2.color("white")
        ball2.turtlesize(6)#ukuran bola
        ball2.penup()#menghilangkan garis
        ball2.goto(-200,-40)#kordinat animasi
        ball2.hideturtle()
        ball2.write(f"OSU !", align="center", font=("inline", 60, "normal"))

        lagu1 = turtle.Turtle()
        lagu1.shape("square")
        lagu1.color("orange")
        lagu1.shapesize(3,16)#panjang,lebar,tebal
        lagu1.penup()#menghilangkan garis
        lagu1.goto(180,260)

        pilih1 = turtle.Turtle()
        pilih1.shape("square")
        pilih1.color("white")
        pilih1.shapesize(3,14)#panjang,lebar,tebal
        pilih1.penup()#menghilangkan garis
        pilih1.goto(180,250)
        pilih1.hideturtle()

        lagu2 = turtle.Turtle()
        lagu2.shape("square")
        lagu2.color("orange")
        lagu2.shapesize(3,16)#panjang,lebar,tebal
        lagu2.penup()#menghilangkan garis
        lagu2.goto(180,190)

        pilih2 = turtle.Turtle()
        pilih2.shape("square")
        pilih2.color("white")
        pilih2.shapesize(3,14)#panjang,lebar,tebal
        pilih2.penup()#menghilangkan garis
        pilih2.goto(180,180)
        pilih2.hideturtle()

        lagu3 = turtle.Turtle()
        lagu3.shape("square")
        lagu3.color("orange")
        lagu3.shapesize(3,16)#panjang,lebar,tebal
        lagu3.penup()#menghilangkan garis
        lagu3.goto(180,120)

        pilih3 = turtle.Turtle()
        pilih3.shape("square")
        pilih3.color("white")
        pilih3.shapesize(3,14)#panjang,lebar,tebal
        pilih3.penup()#menghilangkan garis
        pilih3.goto(180,110)
        pilih3.hideturtle()

        lagu4 = turtle.Turtle()
        lagu4.shape("square")
        lagu4.color("orange")
        lagu4.shapesize(3,16)#panjang,lebar,tebal
        lagu4.penup()#menghilangkan garis
        lagu4.goto(180,50)

        pilih4 = turtle.Turtle()
        pilih4.shape("square")
        pilih4.color("white")
        pilih4.shapesize(3,14)#panjang,lebar,tebal
        pilih4.penup()#menghilangkan garis
        pilih4.goto(180,40)
        pilih4.hideturtle()

        lagu5 = turtle.Turtle()
        lagu5.shape("square")
        lagu5.color("orange")
        lagu5.shapesize(3,16)#panjang,lebar,tebal
        lagu5.penup()#menghilangkan garis
        lagu5.goto(180,-20)

        pilih5 = turtle.Turtle()
        pilih5.shape("square")
        pilih5.color("white")
        pilih5.shapesize(3,14)#panjang,lebar,tebal
        pilih5.penup()#menghilangkan garis
        pilih5.goto(180,-30)
        pilih5.hideturtle()

        lagu6 = turtle.Turtle()
        lagu6.shape("square")
        lagu6.color("orange")
        lagu6.shapesize(3,16)#panjang,lebar,tebal
        lagu6.penup()#menghilangkan garis
        lagu6.goto(180,-90)

        pilih6 = turtle.Turtle()
        pilih6.shape("square")
        pilih6.color("white")
        pilih6.shapesize(3,14)#panjang,lebar,tebal
        pilih6.penup()#menghilangkan garis
        pilih6.goto(180,-100)
        pilih6.hideturtle()

        lagu7 = turtle.Turtle()
        lagu7.shape("square")
        lagu7.color("orange")
        lagu7.shapesize(3,16)#panjang,lebar,tebal
        lagu7.penup()#menghilangkan garis
        lagu7.goto(180,-160)

        pilih7 = turtle.Turtle()
        pilih7.shape("square")
        pilih7.color("white")
        pilih7.shapesize(3,14)#panjang,lebar,tebal
        pilih7.penup()#menghilangkan garis
        pilih7.goto(180,-170)
        pilih7.hideturtle()

        lagu8 = turtle.Turtle()
        lagu8.shape("square")
        lagu8.color("pink")
        lagu8.shapesize(3,16)#panjang,lebar,tebal
        lagu8.penup()#menghilangkan garis
        lagu8.goto(180,-240)

        pilih8 = turtle.Turtle()
        pilih8.shape("square")
        pilih8.color("white")
        pilih8.shapesize(3,14)#panjang,lebar,tebal
        pilih8.penup()#menghilangkan garis
        pilih8.goto(180,-255)
        pilih8.hideturtle()

        def play1():
                dc.clearscreen()
                # Kode untuk inisialisasi musik dan tampilkan panjang durasi musik
                pygame.mixer.init() #memanggil fungsi musik dan audio di python
                pygame.mixer.music.load("Alan Walker - The Spectre (Lyrics).mp3")
                pygame.mixer.music.play()
                # durasilagu = pygame.mixer.Sound("Alan Walker - The Spectre (Lyrics).mp3").get_length() #menentukan durasi lagu dalam satuan detik

                # Memainkan lagu dengan menggunakan metode ontimer() dan membuat fungsi anonim dgn lambda
                # bc.ontimer(lambda: pygame.mixer.music.play(), int(durasilagu) * 2000) #mengatur pemutaran lagu ulang setelah jeda waktu tertentu dr hasil * 2000
                # pythongame.kerangkagame()
                kerangkagame()

        def play2():
                dc.clearscreen()
                # Kode untuk inisialisasi musik dan tampilkan panjang durasi musik
                pygame.mixer.init()
                pygame.mixer.music.load("Alan Walker - Tired (Lyrics) ft. Gavin James.mp3")
                pygame.mixer.music.play()
                # durasilagu = pygame.mixer.Sound("Alan Walker - Tired (Lyrics) ft. Gavin James.mp3").get_length()

                # Memainkan lagu dengan menggunakan metode ontimer() dan membuat fungsi anonim dgn lambda
                # bc.ontimer(lambda: pygame.mixer.music.play(), int(durasilagu) * 2000) #mengatur pemutaran lagu ulang setelah jeda waktu tertentu dr hasil * 2000
                # pythongame.kerangkagame()
                kerangkagame()

        def play3():
                dc.clearscreen()
                # Kode untuk inisialisasi musik dan tampilkan panjang durasi musik
                pygame.mixer.init()
                pygame.mixer.music.load("kaikaikitan - Eve MV.mp3")
                pygame.mixer.music.play()
                # durasilagu = pygame.mixer.Sound("廻廻奇譚 - Eve MV.mp3").get_length()

                # Memainkan lagu dengan menggunakan metode ontimer() dan membuat fungsi anonim dgn lambda
                # bc.ontimer(lambda: pygame.mixer.music.play(), int(durasilagu) * 2000) #mengatur pemutaran lagu ulang setelah jeda waktu tertentu dr hasil * 2000
                # pythongame.kerangkagame()
                kerangkagame()

        def play4():
                dc.clearscreen()
                # Kode untuk inisialisasi musik dan tampilkan panjang durasi musik
                pygame.mixer.init()
                pygame.mixer.music.load("RADWIMPS - suzume.mp3")
                pygame.mixer.music.play()
                # durasilagu = pygame.mixer.Sound("RADWIMPS - すずめ feat.十明 .mp3").get_length()

                # Memainkan lagu dengan menggunakan metode ontimer() dan membuat fungsi anonim dgn lambda
                # bc.ontimer(lambda: pygame.mixer.music.play(), int(durasilagu) * 2000) #mengatur pemutaran lagu ulang setelah jeda waktu tertentu dr hasil * 2000
                # pythongame.kerangkagame()
                kerangkagame()

        def play5():
                dc.clearscreen()
                # Kode untuk inisialisasi musik dan tampilkan panjang durasi musik
                pygame.mixer.init()
                pygame.mixer.music.load("Jujutsu Kaisen Season 2 Shibuya Incident Arc - Opening FULL SPECIALZ By King Gnu (Lyrics).mp3")
                pygame.mixer.music.play()
                # durasilagu = pygame.mixer.Sound("Jujutsu Kaisen Season 2 Shibuya Incident Arc - Opening FULL “SPECIALZ” By King Gnu (Lyrics).mp3").get_length()

                # Memainkan lagu dengan menggunakan metode ontimer() dan membuat fungsi anonim dgn lambda
                # bc.ontimer(lambda: pygame.mixer.music.play(), int(durasilagu) * 2000) #mengatur pemutaran lagu ulang setelah jeda waktu tertentu dr hasil * 2000
                # pythongame.kerangkagame()
                kerangkagame()

        def play6():
                dc.clearscreen()
                # Kode untuk inisialisasi musik dan tampilkan panjang durasi musik
                pygame.mixer.init()
                pygame.mixer.music.load("TK from unravel Music Video(Full Size).mp3")
                pygame.mixer.music.play()
                # durasilagu = pygame.mixer.Sound("TK from 凛として時雨 『unravel』 Music Video(Full Size).mp3").get_length()


                # Memainkan lagu dengan menggunakan metode ontimer() dan membuat fungsi anonim dgn lambda
                # bc.ontimer(lambda: pygame.mixer.music.play(), int(durasilagu) * 2000) #mengatur pemutaran lagu ulang setelah jeda waktu tertentu dr hasil * 2000
                # pythongame.kerangkagame()
                kerangkagame()
        

        def keluar():
                dc.bye()
                # sys.exit()

        gameoverlist.append(1)
        print(gameoverlist)

        dc.listen()

        while True:
                dc.update()
                if len(gameoverlist) == 7:
                    # dc.bye()
                    dc.clearscreen()

                    credit()                                           
                    # creditscene.credit2()
                      
                ball2.write(f"OSU !", align="center", font=("inline", 60, "normal"))
                pilih1.write(f"Pilih lagu", align="center", font=("inline", 20, "normal"))
                pilih2.write(f"Spectre - Alan Walker(1)", align="center", font=("inline", 20, "normal"))
                pilih3.write(f"Tired - Alan Walker(2)", align="center", font=("inline", 20, "normal"))
                pilih4.write(f"廻廻奇譚 - Eve MV(3)", align="center", font=("inline", 20, "normal"))#
                pilih5.write(f"Suzume - RADWIMPS(4)", align="center", font=("inline", 20, "normal"))#
                pilih6.write(f"Specialz - King Gnu(5)", align="center", font=("inline", 20, "normal"))
                pilih7.write(f"Unravel - TK (6)", align="center", font=("inline", 20, "normal"))
                pilih8.write(f"press 7 to EXIT", align="center", font=("inline", 20, "normal"))
                
                turtle.onkey(play1, 1)
                turtle.onkey(play2, 2)
                turtle.onkey(play3, 3) 
                turtle.onkey(play4, 4) 
                turtle.onkey(play5, 5)   
                turtle.onkey(play6, 6) 
                turtle.onkey(keluar, 7) 
                turtle.done()
   
gamemenu()   

